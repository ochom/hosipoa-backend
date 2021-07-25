from django.urls import include, path
from rest_framework.routers import DefaultRouter

from mpesa import views

router = DefaultRouter()
router.register('callback', views.CallbackViewSet)

urlpatterns = [
    path('', include(router.urls))
]
