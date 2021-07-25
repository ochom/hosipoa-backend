from rest_framework import serializers

from accounts.serializers import UserSerializer
from records.serializers import PatientSerializer
from revenue import models


class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceRequest
        fields = '__all__'


class InvoicePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InvoicePayment
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    payments = InvoicePaymentSerializer(many=True, read_only=True)
    service_requests = ServiceRequestSerializer(many=True, read_only=True)
    patient = serializers.SerializerMethodField(read_only=True)
    creator = UserSerializer(source='created_by', read_only=True)

    class Meta:
        model = models.Invoice
        fields = '__all__'

    def get_patient(self, obj):
        return PatientSerializer(instance=obj.patient_id).data


class DepositSerializer(serializers.ModelSerializer):
    patient = serializers.SerializerMethodField()

    class Meta:
        model = models.Deposit
        fields = '__all__'

    def get_patient(self, obj):
        return PatientSerializer(instance=obj.patient_id).data
