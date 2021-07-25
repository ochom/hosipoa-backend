from rest_framework import serializers

from inpatient import models
from organization.models import Ward
from organization.serializers import WardSerializer
from records.models import Patient
from records.serializers import PatientSerializer


class AdmissionSerializer(serializers.ModelSerializer):
    patient = serializers.SerializerMethodField()
    ward = serializers.SerializerMethodField()

    class Meta:
        model = models.Admission
        fields = '__all__'

    def get_patient(self, obj):
        p = Patient.objects.get(pk=obj.patient_id)
        return PatientSerializer(instance=p).data

    def get_ward(self, obj):
        w = Ward.objects.get(pk=obj.ward_id)
        return WardSerializer(instance=w).data


class VitalMonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VitalMonitor
        fields = '__all__'


class InterventionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Intervention
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = '__all__'
