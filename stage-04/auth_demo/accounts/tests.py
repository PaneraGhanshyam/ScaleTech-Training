from django.test import TestCase

from .models import User
from django.contrib.auth.models import Group, Permission


class UserModelTest(TestCase):

    def test_custom_user_creation(self):
        user = User.objects.create_user(
            username="ghanshyam",
            email="ghanshyam@example.com",
            password="testpass123",
            department="Development",
        )

        self.assertEqual(user.username, "ghanshyam")
        self.assertEqual(user.email, "ghanshyam@example.com")
        self.assertEqual(user.department, "Development")
        self.assertTrue(user.check_password("testpass123"))



class RegistrationTest(TestCase):

    def setUp(self):
        self.viewer_group = Group.objects.create(
            name="Viewer"
        )

        permission = Permission.objects.get(
            codename="view_document"
        )

        self.viewer_group.permissions.add(permission)

    def test_registration(self):
        response = self.client.post(
            "/register/",
            {
                "username": "ghanshyam",
                "email": "ghanshyam@example.com",
                "first_name": "Ghanshyam",
                "last_name": "Panera",
                "department": "Development",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
        )

        self.assertRedirects(
            response,
            "/login/",
        )

        user = User.objects.get(
            username="ghanshyam"
        )

        self.assertEqual(
            user.department,
            "Development",
        )

        self.assertTrue(
            user.groups.filter(
                name="Viewer"
            ).exists()
        )   

class LoginTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="ghanshyam",
            password="StrongPass123!",
        )

    def test_login_success(self):

        response = self.client.post(
            "/login/",
            {
                "username": "ghanshyam",
                "password": "StrongPass123!",
            },
        )

        self.assertRedirects(
            response,
            "/dashboard/",
        )

        self.assertTrue(
            response.wsgi_request.user.is_authenticated
        )
        
    def test_login_invalid_password(self):

        response = self.client.post(
            "/login/",
            {
                "username": "ghanshyam",
                "password": "WrongPassword",
            },
        )

        self.assertEqual(
            response.status_code,
            200,
        )

        self.assertFalse(
            response.wsgi_request.user.is_authenticated
        )

class DashboardTest(TestCase):

    def test_dashboard_requires_login(self):

        response = self.client.get(
            "/dashboard/"
        )

        self.assertRedirects(
            response,
            "/login/?next=/dashboard/",
        )
    def setUp(self):
        self.user = User.objects.create_user(
            username="ghanshyam",
            password="StrongPass123!",
        )

    def test_authenticated_user_can_access_dashboard(self):

        self.client.force_login(self.user)

        response = self.client.get(
            "/dashboard/"
        )

        self.assertEqual(
            response.status_code,
            200,
        )