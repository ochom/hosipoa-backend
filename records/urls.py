from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("patients", views.PatientViewSet)
router.register("schemes", views.PatientInsuranceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
