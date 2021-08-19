from mpesa.stk_push import sanitize_phone_number
from django.conf import settings
from django.db import models


class Organization(models.Model):
    organization_name = models.CharField(max_length=100)
    organization_type = models.CharField(max_length=100)
    mfl_code = models.CharField(max_length=100, default="")
    postal_address = models.CharField(max_length=100, default="")
    physical_address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    currency = models.CharField(max_length=20, default="Ksh.")
    is_verified = models.BooleanField(default=False)


class BaseModel(models.Model):
    organization = models.ForeignKey(Organization,
                                     related_name="%(app_label)s_%(class)s",
                                     on_delete=models.CASCADE,
                                     null=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name="%(app_label)s_%(class)s_created_by",
                                   on_delete=models.CASCADE,
                                   null=True)
    updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name="%(app_label)s_%(class)s_updated_by",
                                   on_delete=models.CASCADE,
                                   null=True)

    class Meta:
        abstract = True
