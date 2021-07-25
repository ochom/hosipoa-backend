from rest_framework import serializers

from organization.models import Clinic
from organization.serializers import ClinicSerializer
from outpatient import models
from records.models import Patient
from records.serializers import PatientSerializer
from revenue.models import ServiceRequest
from revenue.serializers import ServiceRequestSerializer


class VitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vital
        fields = '__all__'


class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Observation
        fields = '__all__'


class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Diagnosis
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.SerializerMethodField()
    clinic = serializers.SerializerMethodField()
    vitals = serializers.SerializerMethodField()
    observations = serializers.SerializerMethodField()
    diagnosis = serializers.SerializerMethodField()
    service_requests = serializers.SerializerMethodField()

    class Meta:
        model = models.Appointment
        fields = '__all__'

    def get_patient(self, obj):
        query = Patient.objects.get(pk=obj.patient_id)
        return PatientSerializer(instance=query).data

    def get_clinic(self, obj):
        query = Clinic.objects.get(pk=obj.clinic_id)
        return ClinicSerializer(instance=query).data

    def get_vitals(self, obj):
        query = models.Vital.objects.filter(appointment_id=obj.pk)
        return VitalSerializer(instance=query, many=True).data

    def get_observations(self, obj):
        query = models.Observation.objects.filter(appointment_id=obj.pk)
        return ObservationSerializer(instance=query, many=True).data

    def get_diagnosis(self, obj):
        query = models.Diagnosis.objects.filter(appointment_id=obj.pk)
        return DiagnosisSerializer(instance=query, many=True).data

    def get_service_requests(self, obj):
        query = ServiceRequest.objects.filter(appointment_id=obj.pk)
        return ServiceRequestSerializer(instance=query, many=True).data