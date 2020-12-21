from django.db import IntegrityError
from django.test import TestCase
from rest_framework.test import APITestCase

from main import models
from rest_framework.authtoken.models import Token


class CategoryTest(APITestCase):
    def setUp(self) -> None:
        models.Category.objects.create(name='Best Picture')
        models.Category.objects.create(name='Best Sound Score')

    def test_category_name(self):
        best_picture = models.Category.objects.get(name='Best Picture')
        best_sound_score = models.Category.objects.get(name='Best Sound Score')

        self.assertEqual(str(best_picture), 'Best Picture')
        self.assertEqual(str(best_sound_score), 'Best Sound Score')


class UserTest(TestCase):
    def setUp(self) -> None:
        self.users = [
            {
                'username': 'Dummy1',
                'email': 'dummy1@wonderland.com',
                'password': 'pass',
                'is_staff': True
            },
            {
                'username': 'Dummy2',
                'email': 'dummy2@wonderland.com',
                'password': 'pass',
            },
            {
                'username': 'Dummy3',
                'email': 'dummy3@wonderland.com',
                'password': 'pass',
            }
        ]
        for user in self.users:
            models.UserProfile.objects.create_user(**user)

    def test_user_creation(self):
        for user in self.users:
            user_model = models.UserProfile.objects.get(
                username=user['username']
            )
            self.assertEqual(user_model.username, user['username'])

    def test_create_user_with_existing_email(self):
        with self.assertRaises(IntegrityError):
            models.UserProfile.objects.create(
                username='Dummy4',
                email='dummy1@wonderland.com',
                password='pass'
            )

    def test_create_user_with_existing_username(self):
        with self.assertRaises(IntegrityError):
            models.UserProfile.objects.create(
                username='Dummy1',
                email='dummy5@wonderland.com',
                password='pass'
            )

    def test_token_creation(self):
        for user in self.users:
            try:
                Token.objects.get(user__username=user['username'])
            except Token.DoesNotExist:
                self.fail(f'Token does not exist for user {user["username"]}')

    def test_token_is_valid(self):
        # Checks if the token is returning the right user, with the right data.
        for user in self.users:
            user_model = models.UserProfile.objects.get(
                username=user['username']
            )
            token = models.Token.objects.get(user__username=user['username'])
            response = self.client.get(
                '/users/current_user/',
                HTTP_AUTHORIZATION=f'Token {token}'
            )
            self.assertEqual(response.status_code, 200, response.status_text)
            self.assertEqual(user_model.username, user['username'])
            self.assertEqual(user_model.email, user['email'])
