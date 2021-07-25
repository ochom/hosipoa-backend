from django.db import models


# Create your models here.

class Callback(models.Model):
    body = models.TextField(null=True, blank=True)
