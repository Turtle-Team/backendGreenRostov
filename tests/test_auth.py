import random
import unittest
from unittest import mock

import faker
import requests

class TestRouter(unittest.TestCase):
    def setUp(self):
        self.client = requests.session()
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        self.client.headers.update(headers)
        self.user = {
            'username': 'test',
            'password': 'test',
        }
        self.fake = faker.Faker()


    @mock.patch('jwt.decode')
    def test_refresh_token(self, mock_decode):
        response = self.client.post("http://localhost:5000/user/auth/login", json=self.user)
        refresh = response.json()['refresh_token']
        response = self.client.post("http://localhost:5000/user/auth/refresh", params={"refresh": refresh})
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        response = self.client.post("http://localhost:5000/user/auth/register", json={"username": self.fake.sentence(),
                                                                                      "password":"wrong"})
        self.assertEqual(response.status_code, 200)

    def test_register_user_with_existing_username(self):
        response = self.client.post("http://localhost:5000/user/auth/register", json=self.user)
        self.assertEqual(response.status_code, 400)

    def test_login(self):
        response = self.client.post("http://localhost:5000/user/auth/login", json=self.user)
        self.assertEqual(response.status_code, 200)

    def test_login_with_invalid_credentials(self):
        response = self.client.post("http://localhost:5000/user/auth/login", json={"username":"wrong", "password":"wrong"})
        self.assertEqual(response.status_code, 400)
