from django.urls import include, re_path
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_auth.views import PasswordResetConfirmView

from . import views

router = DefaultRouter()
router.register('groups', views.GroupsViewSet)
router.register('users', views.UsersViewSet)
router.register('signup', views.SignUpViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', views.LoginAPI.as_view(), name='login'),
    path('auth/user/', views.AuthUserAPI.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
