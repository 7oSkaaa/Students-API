from rest_framework import status
from django.test import TestCase

class AccountCreateTest(TestCase):
    
    fixtures = ['parent.yaml', 'account.yaml']
    
    def setUp(self):
        self.endpoint = '/account'
    
    
    def test_case_account_already_registered(self):
        response = self.client.post(f'{self.endpoint}/register/', 
            {
                "username": "7oSkaa",
                "password": "7oSkaa2001", 
                "parent": 1
            }
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST


    def test_create_account_success(self):
        response = self.client.post(f'{self.endpoint}/register/', 
            {
                "username": "Mina",
                "password": "19522001", 
                "parent": 3
            }
        )
        assert response.status_code == status.HTTP_201_CREATED