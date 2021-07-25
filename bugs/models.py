from django.db import models

# Create your models here.
from common.models import BaseModel


class Bug(BaseModel):
    title = models.CharField(max_length=250)
    description = models.TextField()
    is_resolved = models.BooleanField(default=False)

    def replies(self):
        return self.replies


class Replies(BaseModel):
    bug = models.ForeignKey(Bug, related_name="replies", on_delete=models.CASCADE, null=True)
    reply = models.TextField()
