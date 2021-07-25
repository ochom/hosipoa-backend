from rest_framework import serializers

from mpesa import models


class CallbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Callback
        fields = "__all__"
