from django.db import models
# Create your models here.
from django.utils import timezone

from common.models import BaseModel


class Appointment(BaseModel):
    patient_id = models.IntegerField(default=0)
    clinic_id = models.IntegerField(default=0)
    date = models.DateField(default=timezone.now)
    discharge_note = models.TextField(null=True)
    is_discharged = models.BooleanField(default=False)
    discharged_by = models.IntegerField(default=0)


class Vital(BaseModel):
    appointment_id = models.IntegerField(default=0)
    bp_systolic = models.CharField(max_length=10, blank=True, null=True)
    bp_diastolic = models.CharField(max_length=10, blank=True, null=True)
    pulse = models.CharField(max_length=10, blank=True, null=True)
    mass = models.CharField(max_length=10, blank=True, null=True)
    height = models.CharField(max_length=10, blank=True, null=True)
    temperature = models.CharField(max_length=10, blank=True, null=True)
    triage_note = models.TextField(blank=True, null=True)


class Observation(BaseModel):
    appointment_id = models.IntegerField(default=0)
    complaint = models.TextField(blank=True, null=True)
    period = models.CharField(max_length=10, blank=True, null=True)
    period_units = models.CharField(max_length=10, blank=True, null=True)
    pre_med_note = models.TextField(blank=True, null=True)
    physical_examination_note = models.TextField(blank=True, null=True)


class Diagnosis(BaseModel):
    appointment_id = models.IntegerField(default=0)
    disease = models.CharField(max_length=250)
    icd_10 = models.CharField(max_length=20, null=True, blank=True)
