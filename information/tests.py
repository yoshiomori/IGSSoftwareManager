from django.contrib.auth import get_user_model
from django.contrib.auth.models import UserManager
from rest_framework import status
from rest_framework.test import APITestCase


class RestAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        user_model = get_user_model()
        getattr(user_model, 'objects').create_superuser('test', 'teste@teste.com', 'pass')
        super().setUpTestData()

    def test_create_employee(self):
        self.client.login(username='test', password='pass')
        request = self.client.post(
            '/employee/', {'name': 'employee', 'email': 'employee@test.com', 'department': 'Tester'})
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
