import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import unittest
from main import create_app

class TestMeals(unittest.TestCase):
    def test_meal_index(self):
        app = create_app()
        client = app.test_client()

        response = client.get("/meals/")

        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)