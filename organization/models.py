from common.models import BaseModel
from common import constants as CONSTANTS
from django.db import models


class Clinic(BaseModel):
    org = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    appointments = models.IntegerField(default=0)
    appointment_fee = models.IntegerField(default=0)


class Ward(BaseModel):
    org = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    bed_capacity = models.IntegerField(default=0)
    admissions = models.IntegerField(default=0)
    admission_fee = models.IntegerField(default=0)
    daily_fee = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)


class Insurance(BaseModel):
    org = models.IntegerField(default=0)
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=100)
    company_phone = models.CharField(max_length=100)


class Service(BaseModel):
    org = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    department = models.IntegerField(choices=CONSTANTS.DEPARTMENTS)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    rebate = models.DecimalField(max_digits=20, decimal_places=2, default=0)
