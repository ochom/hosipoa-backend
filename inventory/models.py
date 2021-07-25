from django.db import models
from django.utils import timezone

from common.models import BaseModel


class Store(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)


class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField()


class Unit(BaseModel):
    abbr = models.CharField(max_length=10, unique=True)
    desc = models.CharField(max_length=50, unique=True)


class Product(BaseModel):
    store_id = models.ForeignKey(Store, related_name='store_products', on_delete=models.PROTECT)
    name = models.CharField(max_length=100,)
    label = models.CharField(max_length=100, null=True, blank=True)
    unit_id = models.ForeignKey(Unit, on_delete=models.PROTECT)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    startingInventory = models.PositiveIntegerField(default=0)
    inventoryReceived = models.PositiveIntegerField(default=0)
    inventoryShipped = models.PositiveIntegerField(default=0)
    inventoryOnHand = models.PositiveIntegerField(default=0)
    minimumRequired = models.PositiveIntegerField(default=0)


class Requisition(BaseModel):
    store_id = models.ForeignKey(Store, on_delete=models.PROTECT, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, null=True)
    quantity_required = models.PositiveIntegerField(default=0)
    required_by = models.DateField(default=timezone.now)
    quantity_released = models.PositiveIntegerField(default=0)
    is_dispatched = models.BooleanField(default=False)


class Supplier(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Order(BaseModel):
    supplier_id = models.ForeignKey(Supplier, on_delete=models.PROTECT, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, null=True)
    number_ordered = models.PositiveIntegerField(default=0)
    number_received = models.PositiveIntegerField(default=0)
    batch_number = models.CharField(max_length=100, null=True)
    is_supplied = models.BooleanField(default=False)
    cost = models.PositiveIntegerField(default=0)


