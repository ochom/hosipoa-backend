from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from common.models import Organization
from organization import models, serializers


class OrganizationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return Organization.objects.filter(pk=org.pk)


class ClinicViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Clinic.objects.all().order_by("name")
    serializer_class = serializers.ClinicSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Clinic.objects.filter(organization=org)

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class WardsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = models.Ward.objects.all()
    serializer_class = serializers.WardSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Ward.objects.filter(organization=org).order_by('name')

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)



class InsuranceViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Insurance.objects.all().order_by("company_name")
    serializer_class = serializers.InsuranceSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Insurance.objects.filter(organization=org, created_by=self.request.user)

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class ServiceViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Service.objects.all().order_by("name")
    serializer_class = serializers.ServiceSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Service.objects.filter(organization=org)

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
