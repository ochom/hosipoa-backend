from django.contrib.auth.models import AbstractUser
from django.db import models

from common.models import Organization, BaseModel


class Group(BaseModel):
    name = models.CharField(max_length=200)
    # Administration
    can_view_administration = models.BooleanField(default=False)
    can_edit_hospital = models.BooleanField(default=False)
    can_add_clinic = models.BooleanField(default=False)
    can_edit_clinic = models.BooleanField(default=False)
    can_add_ward = models.BooleanField(default=False)
    can_edit_ward = models.BooleanField(default=False)
    can_add_service = models.BooleanField(default=False)
    can_edit_service = models.BooleanField(default=False)
    can_edit_insurance = models.BooleanField(default=False)
    can_add_insurance = models.BooleanField(default=False)
    can_add_user = models.BooleanField(default=False)
    can_edit_user = models.BooleanField(default=False)
    can_add_user_role = models.BooleanField(default=False)
    can_edit_user_role = models.BooleanField(default=False)

    # Inventory
    can_view_inventory = models.BooleanField(default=False)
    can_add_store = models.BooleanField(default=False)
    can_edit_store = models.BooleanField(default=False)
    can_add_product = models.BooleanField(default=False)
    can_edit_product = models.BooleanField(default=False)
    can_add_requisition = models.BooleanField(default=False)
    can_edit_requisition = models.BooleanField(default=False)
    can_add_dispatch = models.BooleanField(default=False)
    can_edit_dispatch = models.BooleanField(default=False)
    can_add_supplier = models.BooleanField(default=False)
    can_edit_supplier = models.BooleanField(default=False)
    can_add_order = models.BooleanField(default=False)
    can_edit_order = models.BooleanField(default=False)

    # Billing
    can_view_billing = models.BooleanField(default=False)
    can_add_invoice = models.BooleanField(default=False)
    can_edit_invoice = models.BooleanField(default=False)
    can_add_deposit = models.BooleanField(default=False)
    can_edit_deposit = models.BooleanField(default=False)

    # Pharmacy
    can_view_pharmacy = models.BooleanField(default=False)
    can_dispense_drug = models.BooleanField(default=False)
    can_add_drug = models.BooleanField(default=False)
    can_edit_drug = models.BooleanField(default=False)

    # Laboratory
    can_view_laboratory = models.BooleanField(default=False)
    can_take_sample = models.BooleanField(default=False)
    can_add_result = models.BooleanField(default=False)
    can_verify_result = models.BooleanField(default=False)

    # Imaging
    can_view_radiology = models.BooleanField(default=False)
    can_start_test = models.BooleanField(default=False)
    can_add_test_result = models.BooleanField(default=False)
    can_verify_test_result = models.BooleanField(default=False)

    # Inpatient and Outpatient
    can_view_ipd_opd = models.BooleanField(default=False)
    can_add_vitals = models.BooleanField(default=False)
    can_add_observation = models.BooleanField(default=False)
    can_add_investigation = models.BooleanField(default=False)
    can_add_diagnosis = models.BooleanField(default=False)
    can_add_prescription = models.BooleanField(default=False)
    can_discharge = models.BooleanField(default=False)
    can_add_review = models.BooleanField(default=False)
    can_add_intervention = models.BooleanField(default=False)

    # Records
    can_view_records = models.BooleanField(default=False)
    can_add_patient = models.BooleanField(default=False)
    can_edit_patient = models.BooleanField(default=False)
    can_add_appointment = models.BooleanField(default=False)
    can_add_admission = models.BooleanField(default=False)
    can_add_scheme = models.BooleanField(default=False)
    can_delete_scheme = models.BooleanField(default=False)
    can_add_service_request = models.BooleanField(default=False)
    can_delete_service_request = models.BooleanField(default=False)


class User(AbstractUser):
    organization = models.ForeignKey(Organization,
                                     related_name="accounts_users",
                                     on_delete=models.CASCADE,
                                     null=True
                                     )
    group = models.ForeignKey(Group, on_delete=models.PROTECT, null=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    is_admin = models.BooleanField('System Admin', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
