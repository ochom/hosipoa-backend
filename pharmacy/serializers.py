from rest_framework import serializers

from pharmacy import models


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Drug
        fields = '__all__'


class DispenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dispense
        fields = '__all__'


class ReorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reorder
        fields = '__all__'
