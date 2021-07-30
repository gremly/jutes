from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_emal_successfull(self):
        email = "my-user@domain.net"
        password = "mysuperpassword"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = "my-user@DOMAIN.NET"

        user = get_user_model().objects.create_user(
            email=email,
            password="superpass"
        )

        self.assertEqual(user.email, "my-user@domain.net")
