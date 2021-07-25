from django.db import models

from common import constants as CONSTANTS
from common.models import BaseModel
from organization.models import Insurance


class Patient(BaseModel):
    fullname = models.CharField(max_length=100)
    id_type = models.IntegerField(choices=CONSTANTS.ID_TYPES, default=1)
    id_no = models.CharField(max_length=100)
    dob = models.DateField()
    sex = models.IntegerField(choices=CONSTANTS.GENDERS, default=0)
    marital_status = models.IntegerField(choices=CONSTANTS.MARITAL_STATUSES, default=0)
    occupation = models.CharField(max_length=100, blank=True)

    phone = models.CharField(max_length=100)
    postal_address = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    sub_county = models.CharField(max_length=100, blank=True)
    ward_estate = models.CharField(max_length=100, blank=True)

    kin_name = models.CharField(max_length=100)
    kin_phone = models.CharField(max_length=100)
    kin_relationship = models.IntegerField(choices=CONSTANTS.KIN_RELATIONSHIPS, default=0)
    kin_id = models.CharField(max_length=100, blank=True)

    is_booked = models.BooleanField(default=False)
    is_admitted = models.BooleanField(default=False)

    class Meta:
        unique_together = ("id_type", "id_no")


class PatientInsurance(BaseModel):
    patient_id = models.ForeignKey(Patient, related_name="patient_insurances", on_delete=models.CASCADE)
    company_id = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=100)
