from django.conf import settings
from django.core.mail import send_mail
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from mpesa import serializers, models


def send_email(message):
    subject = 'MPESA PAYMENT INFO'
    message = str(message)
    from_email = getattr(settings, 'DEFAULT_FROM_EMAIL')
    to = "ochomrichard752@gmail.com"
    send_mail(subject, message, from_email, [to, ], fail_silently=False)


class CallbackViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = models.Callback.objects.all()
    serializer_class = serializers.CallbackSerializer

    def perform_create(self, serializer):
        body = str(self.request.data)
        send_email(body)
        serializer.save(body=body)
