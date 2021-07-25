from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bugs import views

router = DefaultRouter()
router.register("bugs", views.BugsAPI, basename="all bugs")
router.register("replies", views.RepliesAPI, basename="all bugs")

urlpatterns = [
    path('', include(router.urls)),
]
