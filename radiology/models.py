from django.db import models

from common.models import BaseModel


class RadiologyLogbook(BaseModel):
    org = models.IntegerField(default=0)
    patient_id = models.IntegerField(default=0)
    service_request_id = models.IntegerField(default=0)
    investigation = models.CharField(max_length=255, null=True, blank=True)
    result = models.TextField(null=True)
    analysed_at = models.DateTimeField(null=True)
    analysed_by = models.IntegerField(default=0)
    analysis_comment = models.TextField(null=True)
    is_analysed = models.BooleanField(default=False)
