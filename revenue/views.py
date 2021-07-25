# Create your views here.
from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from weasyprint import HTML

from mpesa import stk_push
from records.models import Patient
from records.serializers import PatientSerializer
from revenue import models, serializers


class InvoiceViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Invoice.objects.all()
    serializer_class = serializers.InvoiceSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Invoice.objects.filter(organization=org)

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class UploadDownloadInvoice(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = models.Invoice.objects.all()
    serializer_class = serializers.InvoiceSerializer

    def retrieve(self, request, *args, **kwargs):
        invoice = models.Invoice.objects.get(pk=kwargs['pk'])
        template_path = 'invoice.html'
        total, subtotal = 0, 0
        for req in invoice.service_requests.all():
            total += req.cost
            subtotal += req.cost

        context = {
            "due_date": datetime.now(),
            "title": "Invoice",
            "invoice": invoice,
            "subtotal": subtotal,
            "items_count": invoice.service_requests.count(),
            "grand_total": total,
            "tax": 0
        }

        filename = 'INV[' + str(invoice.pk) + ']-' + invoice.patient_id.fullname + '.pdf'
        html_string = render_to_string(template_path, context)
        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/' + filename)
        design = False
        fs = FileSystemStorage('/tmp')
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=' + filename
            return response if not design else HttpResponse(render_to_string(template_path, context))

    def update(self, request, *args, **kwargs):
        invoice = models.Invoice.objects.get(pk=kwargs['pk'])
        data = self.request.data
        for req in data['service_requests']:
            ser_req = models.ServiceRequest.objects.get(pk=req['id'])
            if ser_req in invoice.service_requests.all():
                ser_req.quantity = req['quantity']
                ser_req.price = req['price']
                ser_req.cost = req['cost']
                ser_req.save()
        return Response("Invoice uploaded successfully", status=status.HTTP_202_ACCEPTED)


class InvoicePaymentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.InvoicePayment.objects.all()
    serializer_class = serializers.InvoicePaymentSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.InvoicePayment.objects.filter(organization=org)

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class DepositViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Deposit.objects.all()
    serializer_class = serializers.DepositSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Deposit.objects.filter(organization=org)

    def perform_create(self, serializer):
        org = self.request.user.organization
        get_object_or_404(Patient, pk=self.request.data['patient_id'])
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        print(serializer)
        serializer.save(updated_by=self.request.user)


class ServiceRequestViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = models.ServiceRequest.objects.all()
    serializer_class = serializers.ServiceRequestSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.ServiceRequest.objects.filter(organization=org).order_by('-pk')

    def perform_create(self, serializer):
        org = self.request.user.organization
        patient = Patient.objects.get(pk=self.request.data['patient_id'])
        invoice, created = models.Invoice.objects.get_or_create(organization=org,
                                                                patient_id=patient,
                                                                status='DRAFT',
                                                                created_by=self.request.user)
        serializer.save(organization=org, created_by=self.request.user, invoice_id=invoice.pk)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_paid or (instance.is_approved and instance.is_served):
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)


class ServiceRequestQueue(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = serializers.ServiceRequestSerializer
    queryset = models.ServiceRequest.objects.all()

    def list(self, request, *args, **kwargs):
        department = request.GET.get('department', 0)
        org = self.request.user.organization
        queue = []
        for patient in Patient.objects.filter(organization=org):
            requests = models.ServiceRequest.objects.filter(is_approved=True,
                                                            is_served=False,
                                                            patient_id=patient.pk,
                                                            department=department)
            p_data = PatientSerializer(instance=patient).data
            request_list = self.serializer_class(requests, many=True).data
            if len(requests) > 0:
                queue.append({'patient': p_data, 'service_requests': request_list})
        return Response(queue, status=status.HTTP_200_OK)


class PaymentQueueViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = models.Invoice.objects.all()
    serializer_class = serializers.InvoiceSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Invoice.objects.filter(organization=org,
                                             status='DRAFT',
                                             service_requests__is_approved=False).distinct()

    def create(self, request, *args, **kwargs):
        data = self.request.data
        invoice = models.Invoice.objects.get(pk=data['invoice_id'])
        service_requests = data['service_requests']
        payment_method = data['payment_method']
        transaction_code = data['transaction_code']
        total = 0

        for req in service_requests:
            service_req = models.ServiceRequest.objects.get(pk=req['id'])
            total += service_req.cost

        if payment_method == 'mobile':
            phone = self.request.data['transaction_code']
            mpesa_response = stk_push.push(phone, total, invoice.pk)
            print(mpesa_response)
            if not mpesa_response['success']:
                return Response("payment not successful", status=status.HTTP_402_PAYMENT_REQUIRED)

        payment = models.InvoicePayment.objects.create(
            invoice=invoice,
            amount_paid=total,
            account_name=payment_method,
            date_paid=datetime.now()
        )

        for req in service_requests:
            service_req = models.ServiceRequest.objects.get(pk=req['id'])
            service_req.is_approved = True
            service_req.payment_method = payment_method
            service_req.transaction_code = transaction_code
            service_req.is_paid = True if (payment_method != "insurance") else False
            service_req.payment_received_by = self.request.user
            service_req.save()
            total += service_req.cost
        return Response("payment saved", status=status.HTTP_201_CREATED)
