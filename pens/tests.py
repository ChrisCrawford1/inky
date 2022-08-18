from django.contrib.auth.models import User
from django.test import TestCase

from brands.models import Brand


class PenCreationTest(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(username="john", email="john@test.com", password="supersecurepasswordwow")

    def test_user_is_redirected_if_accessing_creation_while_not_logged_in(self):
        response = self.client.get("/pens/create")
        self.assertEqual(response.status_code, 302)


