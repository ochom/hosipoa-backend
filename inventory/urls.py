from django.urls import path, include
from inventory import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stores', views.StoreViewSet)
router.register('categories', views.CategoryViewSet)
router.register('units', views.UnitViewSet)
router.register('products', views.ProductViewSet)
router.register('requisitions', views.RequisitionViewSet)
router.register('suppliers', views.SupplierViewSet)
router.register('orders', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls))
]
