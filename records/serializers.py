from rest_framework import serializers

from organization.models import Clinic, Ward
from organization.serializers import InsuranceSerializer, ClinicSerializer, WardSerializer
from records import models
from django.apps import apps

Appointment = apps.get_model('outpatient', 'Appointment')
Admission = apps.get_model('inpatient', 'Admission')


class PatientInsuranceSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()

    class Meta:
        model = models.PatientInsurance
        fields = "__all__"

    def get_company(self, obj):
        c = obj.company_id
        return InsuranceSerializer(instance=c).data


class AppointmentSerializer(serializers.ModelSerializer):
    clinic = serializers.SerializerMethodField()
    class Meta:
        model = Appointment
        fields = '__all__'

    def get_clinic(self, obj):
        query = Clinic.objects.get(pk=obj.clinic_id)
        return ClinicSerializer(instance=query).data


class AdmissionSerializer(serializers.ModelSerializer):
    ward = serializers.SerializerMethodField()

    class Meta:
        model = Admission
        fields = '__all__'

    def get_ward(self, obj):
        query = Ward.objects.get(pk=obj.ward_id)
        return WardSerializer(instance=query).data


class PatientSerializer(serializers.ModelSerializer):
    insurance = PatientInsuranceSerializer(source='patient_insurances', many=True, read_only=True)
    appointments = serializers.SerializerMethodField()
    admissions = serializers.SerializerMethodField()

    def get_appointments(self, obj):
        query = Appointment.objects.filter(patient_id=obj.pk)
        return AppointmentSerializer(instance=query, many=True).data

    def get_admissions(self, obj):
        query = Admission.objects.filter(patient_id=obj.pk)
        return AdmissionSerializer(instance=query, many=True).data

    class Meta:
        model = models.Patient
        fields = "__all__"
