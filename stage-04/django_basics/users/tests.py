from django.test import TestCase
from .models import UserProfile


class UserProfileTestCase(TestCase):

    def test_user_creation(self):
        user = UserProfile.objects.create(
            name="Ghanshyam",
            email="ghanshyam@example.com",
            age=22
        )

        self.assertEqual(user.name, "Ghanshyam")
        self.assertEqual(user.age, 22)