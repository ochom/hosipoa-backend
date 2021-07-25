from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from common.models import Organization
from organization.serializers import OrganizationSerializer
from . import models, serializers


def send_success_email(fullname, email, phone):
    html_message = loader.render_to_string(
        'registration_successful.html',
        {
            'full_name': fullname,
            'email': email,
            'password': phone[:4] + '******'
        }
    )
    subject = 'Registration Successful'
    from_email = getattr(settings, 'DEFAULT_FROM_EMAIL')
    to = (email,)
    message = 'Registration is successful'
    send_mail(subject, message, from_email, to, fail_silently=True, html_message=html_message)

    # notify admins of new sign up
    msg = "Dear Admin, A new User %s with email address %s has sign up to Hosipoa" % (fullname, email)
    send_mail("New User Signup", msg, from_email, ("support@lysofts.co.ke",), fail_silently=False)


class SignUpViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def perform_create(self, serializer):
        org_serializer = serializer.save()

        self.request.data['username'] = self.request.data['first_name'] + " " + self.request.data['last_name']
        self.request.data['password'] = self.request.data['phone']
        self.request.data['is_admin'] = True
        user_sr = serializers.UserSerializer(data=self.request.data)
        user_sr.is_valid(raise_exception=True)
        user_sr.save(organization=org_serializer)
        send_success_email(self.request.data['username'], self.request.data['email'], self.request.data['phone'])


class GroupsViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = models.Group.objects.all()
    serializer_class = serializers.GroupSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.Group.objects.filter(organization=org).order_by("name")

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org, created_by=self.request.user)


class UsersViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        org = self.request.user.organization
        return models.User.objects.filter(organization=org).order_by("username")

    def perform_create(self, serializer):
        org = self.request.user.organization
        serializer.save(organization=org)


class AuthUserAPI(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UserSerializer

    def get(self, request, *args, **kwargs):
        user = self.request.user
        organization = self.request.user.organization
        if organization.is_verified:
            return Response({
                "user": self.serializer_class(instance=user).data,
                "token": str(Token.objects.get_or_create(user=user)[0]),
            })
        else:
            return Response("Organization not verified", status=status.HTTP_401_UNAUTHORIZED)


class LoginAPI(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        organization = user.organization

        if organization is not None and organization.is_verified:
            return Response({
                "user": serializers.UserSerializer(instance=user).data,
                "token": str(Token.objects.get_or_create(user=user)[0]),
            })
        else:
            return Response("Organization not verified", status=status.HTTP_401_UNAUTHORIZED)


class Logout(APIView):
    permission_classes = [IsAuthenticated, ]

    # Use expiring tokens when making permanent logout.. Read this later
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
