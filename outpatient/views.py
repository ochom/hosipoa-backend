# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from organization.models import Clinic
from outpatient import models, serializers
from records.models import Patient


class AppointmentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Appointment.objects.filter(organization=org)

    def perform_create(self, serializer):
        org = self.request.user.organization
        clinic = Clinic.objects.get(pk=self.request.data['clinic_id'])
        clinic.appointments += 1
        clinic.save()
        patient = Patient.objects.get(pk=self.request.data['patient_id'])
        patient.is_booked = True
        patient.save()
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()
        data = self.request.data
        if 'is_discharged' in data:
            p = Patient.objects.get(pk=instance.patient_id)
            p.is_booked = False
            p.save()


class VitalViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Vital.objects.all()
    serializer_class = serializers.VitalSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Vital.objects.filter(organization=org)

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)


class ObservationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Observation.objects.all()
    serializer_class = serializers.ObservationSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Observation.objects.filter(organization=org)

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)


class DiagnosisViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Diagnosis.objects.all()
    serializer_class = serializers.DiagnosisSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Diagnosis.objects.filter(organization=org)

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)
