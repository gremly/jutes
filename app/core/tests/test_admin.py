from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="super-user@domain.net",
            password="superpass",
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@domain.net",
            password="userpass234",
            name="Juan Perez",
        )

    def test_users_listed(self):
        url = reverse("admin:core_user_changelist")

        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_edit_user_page(self):
        url = reverse("admin:core_user_change", args=[self.user.id])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        url = reverse("admin:core_user_add")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
