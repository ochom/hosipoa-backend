from common.models import Organization
from django.test import TestCase


class OrganizationTestCase(TestCase):
    def setUp(self):
        Organization.objects.create(
            organization_name="Test Hospital",
            organization_type="Clinic",
            mfl_code="RAD-00100",
            postal_address="00100, Nairobi",
            physical_address="Test Street",
            email="test@email.com",
            phone="254708113456",
            currency="UG. SH"
        )

    def test_organization_created(self):
        org = Organization.objects.get(organization_name="Test Hospital")
        self.assertEqual(org.phone, "254708113456")

    def test_organization_update(self):
        org = Organization.objects.get(organization_name="Test Hospital")
        org.is_verified = True
        org.save()
        self.assertEqual(org.is_verified, True)
