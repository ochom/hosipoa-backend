from django.test import SimpleTestCase
from django.urls import reverse


class TestUrls(SimpleTestCase):
    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(url, '/api/auth/login/')
