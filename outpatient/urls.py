from django.urls import path, include
from rest_framework.routers import DefaultRouter

from outpatient import views

router = DefaultRouter()
router.register("appointments", views.AppointmentViewSet)
router.register("vitals", views.VitalViewSet)
router.register("observations", views.ObservationViewSet)
router.register("diagnosis", views.DiagnosisViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

