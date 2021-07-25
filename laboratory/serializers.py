from rest_framework import serializers

from laboratory.models import Logbook


class LogbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logbook
        fields = '__all__'
