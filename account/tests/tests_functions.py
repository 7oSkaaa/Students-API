from rest_framework import status
from django.test import TestCase

class AccountValidatorTest(TestCase):
    
    fixtures = ['parent.yaml', 'account.yaml']
    
    def setUp(self):
        self.endpoint = '/account'

    def test_password_validator(self):
        response = self.client.post(f'{self.endpoint}/register/', 
            {
                "username": "Ali",
                "password": "1952", 
                "parent": 3
            }
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        