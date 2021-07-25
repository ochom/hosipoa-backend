# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from laboratory import serializers, models
from revenue.models import ServiceRequest


class LogbookViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Logbook.objects.all()
    serializer_class = serializers.LogbookSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Logbook.objects.filter(organization=org).order_by('-pk')

    def perform_create(self, serializer):
        org = self.request.user.organization
        service_req = ServiceRequest.objects.get(pk=self.request.data['service_request_id'])
        service_req.is_served = True
        service_req.save()
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()
        if 'result' in self.request.data:
            service_req = ServiceRequest.objects.get(pk=instance.service_request_id)
            service_req.description = self.request.data['result']
            service_req.is_served = True
            service_req.save()
        serializer.save(updated_by=self.request.user)
