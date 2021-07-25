from django.db import models

# Create your models here.
from common.models import BaseModel


class Drug(BaseModel):
    org = models.IntegerField(default=0)
    brand_name = models.CharField(max_length=100, null=True, blank=True)
    act_ing_name = models.CharField(max_length=100, null=True, blank=True)
    exc_name = models.CharField(max_length=100, null=True, blank=True)
    act_ing_short_name = models.CharField(max_length=100, null=True, blank=True)
    formula = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)
    form = models.CharField(max_length=100, null=True, blank=True)
    smell = models.CharField(max_length=100, null=True, blank=True)
    taste = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    units = models.CharField(max_length=100, null=True, blank=True)
    reorder_level = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=20, decimal_places=2)


class Reorder(BaseModel):
    org = models.IntegerField(default=0)
    drug_id = models.IntegerField(default=0)
    drug_name = models.CharField(max_length=200, null=True, blank=True)
    quantity_before = models.IntegerField(default=0)
    new_stock_quantity = models.IntegerField(default=0)
    quantity_after = models.IntegerField(default=0)
    batch_number = models.CharField(max_length=200, unique=True)
    expiry_date = models.DateField()


class Dispense(BaseModel):
    org = models.IntegerField(default=0)
    drug_id = models.IntegerField(default=0)
    quantity_before = models.IntegerField(default=0)
    dispensed_quantity = models.IntegerField(default=0)
    quantity_after = models.IntegerField()
