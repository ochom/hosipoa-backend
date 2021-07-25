from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordResetForm
from rest_framework import serializers

from accounts import models
from django.conf import settings
from django.utils.translation import gettext as _


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    rights = serializers.SerializerMethodField()

    class Meta:
        model = models.User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def get_rights(self, obj):
        return GroupSerializer(instance=obj.group).data

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = models.User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password_reset_form_class = PasswordResetForm

    def validate_email(self, value):
        reset_form = self.password_reset_form_class(data=self.initial_data)
        if not reset_form.is_valid():
            raise serializers.ValidationError(_('Error'))

        if not models.User.objects.filter(email=value).exists():
            raise serializers.ValidationError(_('Invalid e-mail address'))
        return value

    def save(self):
        request = self.context.get('request')
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            'subject_template_name': 'password_reset_subject.txt',
            'email_template_name': 'password_reset_email.html',
            'html_email_template_name': 'password_reset_email.html',

            'request': request,
        }
        self.reset_form.save(**opts)
