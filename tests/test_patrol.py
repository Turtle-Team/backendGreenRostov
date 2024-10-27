import unittest
import requests

class TestAchievements(unittest.TestCase):

    def setUp(self):
        self.base_url = 'http://localhost:5000/api'

    def test_get_achievements(self):
        response = requests.get(f'{self.base_url}/me')
        self.assertEqual(response.status_code, 200)

    def test_answer(self):
        data = {'answers': 'test answers'}
        response = requests.post(f'{self.base_url}/1', json=data)
        self.assertEqual(response.status_code, 200)

    def test_answer_border_case(self):
        data = {'answers': ''}
        response = requests.post(f'{self.base_url}/1', json=data)
        self.assertEqual(response.status_code, 200)

    def test_answer_not_found(self):
        data = {'answers': 'test answers'}
        response = requests.post(f'{self.base_url}/10000', json=data)
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()

