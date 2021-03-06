from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = "rohit@gmail.com"
        password = "Test@1234"

        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = "rohu.billu22@GMAIL.COM"
        user = get_user_model().objects.create_user(email, "Test@1234")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "Test@1234")

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            "rohu.billu22@gmail.com", "Test@1234"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
