from rest_framework import serializers

from radiology.models import RadiologyLogbook as Logbook


class LogbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logbook
        fields = '__all__'
