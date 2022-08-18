from django.contrib.auth.models import User
from django.test import TestCase


class URLTests(TestCase):
    def test_homepage_returns_302_when_logged_out(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)

    def test_login_returns_200(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/login.html")


class UserLoggedInTest(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(username="john", email="john@test.com", password="supersecurepasswordwow")

    def test_user_can_login_and_receive_200(self):
        self.client.login(username="john", password="supersecurepasswordwow")
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context["user"]), "john")
        self.assertTemplateUsed(response, 'homepage.html')

    def test_returns_error_for_wrong_password(self):
        self.client.login(username="john", password="wrong_password_oops")
        response = self.client.get("/")

        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(response.context, None)


