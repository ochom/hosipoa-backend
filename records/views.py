# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from records import models, serializers


class PatientViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = models.Patient.objects.all().order_by("fullname")
    serializer_class = serializers.PatientSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Patient.objects.filter(organization=org)

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)


class PatientInsuranceViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.PatientInsurance.objects.all()
    serializer_class = serializers.PatientInsuranceSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.PatientInsurance.objects.filter(organization=org)

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)
