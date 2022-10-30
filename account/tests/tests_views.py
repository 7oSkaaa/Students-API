from rest_framework import status
from django.test import TestCase

class AccountViewTest(TestCase):
    
    fixtures = ['data.yaml']
    
    def setUp(self):
        self.endpoint = '/account'
        
    def test_login_success(self):
        response = self.client.post(f'{self.endpoint}/login/', 
            {
                "username": "7oSkaa",
                "password": "7oSkaa2001",
                "parent": 1
            }
        )
        assert response.status_code == status.HTTP_200_OK
        
    def test_login_failed(self):
        response = self.client.post(f'{self.endpoint}/login/', 
            {
                "username": "7oSkaa",
                "password": "7oSkaa2002",
                "parent": 1
            }
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND