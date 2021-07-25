from rest_framework import serializers

from accounts.serializers import UserSerializer
from bugs import models


class RepliesSerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField()

    class Meta:
        model = models.Replies
        fields = "__all__"

    def get_creator(self, obj):
        return UserSerializer(instance=obj.created_by).data


class BugSerializer(serializers.ModelSerializer):
    replies = RepliesSerializer(many=True, read_only=True)
    creator = serializers.SerializerMethodField()

    class Meta:
        model = models.Bug
        fields = "__all__"

    def get_creator(self, obj):
        return UserSerializer(instance=obj.created_by).data
