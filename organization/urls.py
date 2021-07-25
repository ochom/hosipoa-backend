from django.urls import path, include
from organization import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hospital', views.OrganizationViewSet)
router.register('clinics', views.ClinicViewSet)
router.register('wards', views.WardsViewSet)
router.register('insurance', views.InsuranceViewSet)
router.register('service', views.ServiceViewSet)

urlpatterns = [
    path('', include(router.urls))
]
