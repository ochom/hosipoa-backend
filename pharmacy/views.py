# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from pharmacy import serializers, models
from revenue.models import ServiceRequest


class DrugViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = models.Drug.objects.all()
    serializer_class = serializers.DrugSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Drug.objects.filter(organization=org).order_by('brand_name')

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)


class ReOrderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = models.Reorder.objects.all()
    serializer_class = serializers.ReorderSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Reorder.objects.filter(organization=org).order_by('-pk')

    def perform_create(self, serializer):
        org = self.request.user.organization
        drug = models.Drug.objects.get(pk=int(self.request.data['drug_id']))
        quantity_before = drug.quantity
        quantity_after = quantity_before + int(self.request.data['new_stock_quantity'])

        drug.quantity = quantity_after
        drug.save()

        serializer.save(organization=org,
                        drug_name=drug.brand_name,
                        quantity_before=quantity_before,
                        quantity_after=quantity_after,
                        created_by=self.request.user)


class DispenseViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = models.Dispense.objects.all()
    serializer_class = serializers.DispenseSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Dispense.objects.filter(organization=org).order_by('-pk')

    def create(self, request, *args, **kwargs):
        service_req = ServiceRequest.objects.get(pk=int(request.data['service_request_id']))
        drug = models.Drug.objects.get(pk=service_req.service_id)
        q_before = drug.quantity
        q_after = drug.quantity - service_req.quantity

        if drug.quantity >= service_req.quantity:
            drug.quantity -= service_req.quantity
            drug.save()
            request.data['quantity_before'] = q_before
            request.data['dispensed_quantity'] = service_req.quantity
            request.data['quantity_after'] = q_after
            request.data['drug_id'] = drug.pk
            request.data['org'] = drug.org

            # update service request as served
            service_req.is_served = True
            service_req.save()
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response("Quantity in store is less than prescription", status=status.HTTP_403_FORBIDDEN)
