from allauth.socialaccount.models import SocialApp
from django.conf import settings
from django.contrib.sites.models import Site
from django.test import TestCase


class AuthPagesWithoutGoogleAppTests(TestCase):
    def setUp(self):
        SocialApp.objects.all().delete()

    def test_login_page_renders_without_google_button(self):
        response = self.client.get("/login/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")
        self.assertNotContains(response, "Use Google")

    def test_register_page_renders_without_google_button(self):
        response = self.client.get("/register/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Register")
        self.assertNotContains(response, "Use Google")


class AuthPagesWithGoogleAppTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        site, _ = Site.objects.update_or_create(
            id=settings.SITE_ID,
            defaults={"domain": "testserver", "name": "testserver"},
        )
        social_app, _ = SocialApp.objects.get_or_create(
            provider="google",
            name="Google",
            client_id="test-client-id",
            secret="test-secret",
        )
        social_app.sites.add(site)

    def test_login_page_shows_google_button(self):
        response = self.client.get("/login/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Use Google")

    def test_register_page_shows_google_button(self):
        response = self.client.get("/register/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Use Google")
