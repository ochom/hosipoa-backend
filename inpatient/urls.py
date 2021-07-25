from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inpatient import views

router = DefaultRouter()
router.register('admissions', views.AdmissionViewSet)
router.register('vitals', views.VitalsViewSet)
router.register('interventions', views.InterventionViewSet)
router.register('reviews', views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
