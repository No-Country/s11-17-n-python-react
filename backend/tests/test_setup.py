from rest_framework import status
from rest_framework.test import APITestCase

class TestSetUp(APITestCase):

    def setUp(self):
        from apps.users.models import User

        self.create_user_url = '/api-users/users/'
        response = self.client.post(
            self.create_user_url,
            
            {
                "username": "javier",
                "email": "javier@mail.com",
                "password": "contraseña"
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.login_url = '/login/'
        response = self.client.post(
            self.login_url,
            
            {
                "username": "javier",
                "password": "contraseña"
            },
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        return super().setUp()   

    def test_login(self):
        pass
