from rest_framework import serializers

from common.models import Organization
from organization import models


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clinic
        fields = "__all__"


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ward
        fields = '__all__'


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Insurance
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = "__all__"
