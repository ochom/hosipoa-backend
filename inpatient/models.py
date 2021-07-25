from django.db import models

# Create your models here.
from common.models import BaseModel


class Admission(BaseModel):
    patient_id = models.IntegerField(default=0)
    ward_id = models.IntegerField(default=0)
    bed = models.CharField(max_length=100, null=True)
    admission_notes = models.TextField(null=True, blank=True)
    discharge_note = models.TextField(null=True)
    is_discharged = models.BooleanField(default=False)
    discharged_by = models.IntegerField(default=0)


class VitalMonitor(BaseModel):
    admission_id = models.IntegerField(default=0)
    bp_systolic = models.CharField(max_length=10, blank=True, null=True)
    bp_diastolic = models.CharField(max_length=10, blank=True, null=True)
    pulse = models.CharField(max_length=10, blank=True, null=True)
    mass = models.CharField(max_length=10, blank=True, null=True)
    height = models.CharField(max_length=10, blank=True, null=True)
    temperature = models.CharField(max_length=10, blank=True, null=True)
    triage_note = models.TextField(blank=True, null=True)
    

class Intervention(BaseModel):
    admission_id = models.IntegerField(default=0)
    note = models.TextField(null=False, blank=False)


class Review(BaseModel):
    admission_id = models.IntegerField(default=0)
    condition = models.TextField(null=False, blank=False)
    note = models.TextField(null=False, blank=False)
