from allauth.socialaccount.models import SocialApp
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.test import TestCase


def user_count() -> int:
    return get_user_model().objects.count()


class SanityTests(TestCase):
    def test_false_is_false(self):
        self.assertFalse(False)

    def test_true_is_true(self):
        self.assertTrue(True)

    def test_one_plus_one_equals_two(self):
        self.assertEqual(1 + 1, 2)


class RegisterPageBaseTest(TestCase):
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


class CreateSingleUserTest(RegisterPageBaseTest):
    def setUp(self) -> None:
        self.username = "testRegister"
        self.email = "testRegister@email.com"
        self.password = "qJXyNRZPn6Zhh623"
        self.first_name = "firstname"
        self.last_name = "lastname"

    def test_main(self):
        initial_count = user_count()

        response = self.client.post(
            "/register/",
            data={
                "username": self.username,
                "email": self.email,
                "password1": self.password,
                "password2": self.password,
                "first_name": self.first_name,
                "last_name": self.last_name,
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(user_count(), initial_count + 1)


class EmptyPasswordTest(RegisterPageBaseTest):
    def setUp(self) -> None:
        self.username = "0testuser2"
        self.email = "testuser@email.com"
        self.password = ""
        self.first_name = "firstname"
        self.last_name = "lastname"

    def test_main(self):
        initial_count = user_count()

        response = self.client.post(
            "/register/",
            data={
                "username": self.username,
                "email": self.email,
                "password1": self.password,
                "password2": self.password,
                "first_name": self.first_name,
                "last_name": self.last_name,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_count(), initial_count)


class EmptyEmailTest(RegisterPageBaseTest):
    def setUp(self) -> None:
        self.username = "0testuser2"
        self.email = ""
        self.password = "qJXyNRZPn6Zhh623"
        self.first_name = "firstname"
        self.last_name = "lastname"

    def test_main(self):
        initial_count = user_count()

        response = self.client.post(
            "/register/",
            data={
                "username": self.username,
                "email": self.email,
                "password1": self.password,
                "password2": self.password,
                "first_name": self.first_name,
                "last_name": self.last_name,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_count(), initial_count)


class CreateTwoAccountsTest(RegisterPageBaseTest):
    def setUp(self) -> None:
        self.username = "testuser1001"
        self.email = "testuser1001@email.com"
        self.password = "qJXyNRZPn6Zhh623"

        self.username2 = "testuser10022"
        self.email2 = "testuser1002@email.com"
        self.password2 = "qJXyNRZPn6Zhh6232"

        self.first_name = "firstname"
        self.last_name = "lastname"

    def test_main(self):
        initial_count = user_count()

        response = self.client.post(
            "/register/",
            data={
                "username": self.username,
                "email": self.email,
                "password1": self.password,
                "password2": self.password,
                "first_name": self.first_name,
                "last_name": self.last_name,
            },
        )
        self.assertEqual(response.status_code, 302)

        response = self.client.post(
            "/register/",
            data={
                "username": self.username2,
                "email": self.email2,
                "password1": self.password2,
                "password2": self.password2,
                "first_name": self.first_name,
                "last_name": self.last_name,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(user_count(), initial_count + 2)


class CreateTwoIdenticalAccountsTest(RegisterPageBaseTest):
    def setUp(self) -> None:
        self.username = "testuser1110"
        self.email = "testusertestuser1110@email.com"
        self.password = "qJXyNRZPn6Zhh623"
        self.first_name = "firstname"
        self.last_name = "lastname"

    def test_main(self):
        initial_count = user_count()

        response = self.client.post(
            "/register/",
            data={
                "username": self.username,
                "email": self.email,
                "password1": self.password,
                "password2": self.password,
                "first_name": self.first_name,
                "last_name": self.last_name,
            },
        )
        self.assertEqual(response.status_code, 302)

        response = self.client.post(
            "/register/",
            data={
                "username": self.username,
                "email": self.email,
                "password1": self.password,
                "password2": self.password,
                "first_name": self.first_name,
                "last_name": self.last_name,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_count(), initial_count + 1)


class CreateUserWithEmailAsPasswordTest(RegisterPageBaseTest):
    def setUp(self) -> None:
        self.username = "testuser1111"
        self.email = "testuser1111@email.com"
        self.password = "testuser1111@email.com"
        self.first_name = "firstname"
        self.last_name = "lastname"

    def test_main(self):
        initial_count = user_count()

        response = self.client.post(
            "/register/",
            data={
                "username": self.username,
                "email": self.email,
                "password1": self.password,
                "password2": self.password,
                "first_name": self.first_name,
                "last_name": self.last_name,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_count(), initial_count)


class CreateUserWithWrongFirstNameTest(RegisterPageBaseTest):
    def setUp(self) -> None:
        self.username = "testuser1112"
        self.email = "testuser1112@email.com"
        self.password = "qJXyNRZPn6Zhh623"
        self.first_name1 = "firstname01"
        self.first_name2 = "invalid@@name"
        self.last_name = "lastname"

    def test_numeric_first_name(self):
        initial_count = user_count()

        response = self.client.post(
            "/register/",
            data={
                "username": self.username,
                "email": self.email,
                "password1": self.password,
                "password2": self.password,
                "first_name": self.first_name1,
                "last_name": self.last_name,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_count(), initial_count)

    def test_weird_characters_first_name(self):
        initial_count = user_count()

        response = self.client.post(
            "/register/",
            data={
                "username": self.username,
                "email": self.email,
                "password1": self.password,
                "password2": self.password,
                "first_name": self.first_name2,
                "last_name": self.last_name,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_count(), initial_count)


class CreateUserWithWrongLastNameTest(RegisterPageBaseTest):
    def setUp(self) -> None:
        self.username = "testuser1115"
        self.email = "testuser1115@email.com"
        self.password = "qJXyNRZPn6Zhh623"
        self.first_name = "firstname"
        self.last_name1 = "lastname02"
        self.last_name2 = "invalid@@last"

    def test_numeric_last_name(self):
        initial_count = user_count()

        response = self.client.post(
            "/register/",
            data={
                "username": self.username,
                "email": self.email,
                "password1": self.password,
                "password2": self.password,
                "first_name": self.first_name,
                "last_name": self.last_name1,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_count(), initial_count)

    def test_weird_characters_last_name(self):
        initial_count = user_count()

        response = self.client.post(
            "/register/",
            data={
                "username": self.username,
                "email": self.email,
                "password1": self.password,
                "password2": self.password,
                "first_name": self.first_name,
                "last_name": self.last_name2,
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_count(), initial_count)
