from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from inpatient import serializers, models
from organization.models import Ward
from records.models import Patient


class AdmissionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = models.Admission.objects.all()
    serializer_class = serializers.AdmissionSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Admission.objects.filter(organization=org)

    def perform_create(self, serializer):
        org = self.request.user.organization
        ward = Ward.objects.get(pk=self.request.data['ward_id'])
        ward.admissions += 1
        ward.save()
        patient = Patient.objects.get(pk=self.request.data['patient_id'])
        patient.is_admitted = True
        patient.save()
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()
        data = self.request.data
        if 'is_discharged' in data:
            p = Patient.objects.get(pk=instance.patient_id)
            p.is_admitted = False
            p.save()


class VitalsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = models.VitalMonitor.objects.all()
    serializer_class = serializers.VitalMonitorSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.VitalMonitor.objects.filter(organization=org)

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class InterventionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = models.Intervention.objects.all()
    serializer_class = serializers.InterventionSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Intervention.objects.filter(organization=org)

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class ReviewViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Review.objects.filter(organization=org)

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

