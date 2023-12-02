from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
import pytest

class TestCreateCollection(TestCase):
   # @pytest.mark.skip
    def test_if_user_is_anonymous_returns_401(self):
        client = APIClient()
        response = client.post('/api/CityViewSet/', {'name': 'a'})
        # Check if the response status code is 401 Unauthorized
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
