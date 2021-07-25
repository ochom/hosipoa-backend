from django.db import models

from accounts.models import User
from common import constants as CONSTANTS
from common.models import BaseModel
from records.models import Patient

invoice_status = [
    ('DRAFT', 'draft'),
    ('BILLED', 'billed'),
    ('CLEARED', 'cleared')
]


class Invoice(BaseModel):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=invoice_status, default="DRAFT")

    class Meta:
        unique_together = ('patient_id', 'status')


class InvoicePayment(BaseModel):
    invoice = models.ForeignKey(Invoice, related_name="payments", on_delete=models.CASCADE)
    amount_paid = models.PositiveIntegerField(default=0)
    account_name = models.CharField(max_length=250)
    date_paid = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)


class Deposit(BaseModel):
    patient_id = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    notes = models.TextField(null=True, blank=True)


class ServiceRequest(BaseModel):
    invoice = models.ForeignKey(Invoice, related_name="service_requests", null=True, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, null=True, on_delete=models.CASCADE)
    appointment_id = models.IntegerField(default=0)
    admission_id = models.IntegerField(default=0)
    service_id = models.IntegerField(default=0)
    service_name = models.CharField(max_length=200)
    department = models.IntegerField(choices=CONSTANTS.DEPARTMENTS, default=0)
    description = models.TextField(null=True, blank=True)  # for results or prescription description
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    is_served = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    transaction_code = models.CharField(max_length=100, null=True, blank=True)
    payment_received_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
