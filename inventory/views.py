from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from inventory import models, serializers


class StoreViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Store.objects.all()
    serializer_class = serializers.StoreSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Store.objects.filter(organization=org).order_by('name')

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Category.objects.filter(organization=org).order_by('name')

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class UnitViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Unit.objects.all()
    serializer_class = serializers.UnitSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Unit.objects.filter(organization=org).order_by('abbr')

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class ProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Product.objects.filter(organization=org).order_by('name')

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class RequisitionViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Requisition.objects.all()
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Requisition.objects.filter(organization=org)

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class SupplierViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Supplier.objects.filter(organization=org).order_by('name')

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class OrderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Order.objects.filter(organization=org)

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
