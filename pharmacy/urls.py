from django.urls import path, include
from rest_framework.routers import DefaultRouter

from pharmacy import views
router = DefaultRouter()
router.register('drugs', views.DrugViewSet)
router.register('reorders', views.ReOrderViewSet)
router.register('dispense', views.DispenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
