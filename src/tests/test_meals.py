import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import unittest
from main import create_app, db

class TestMeals(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()

        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db", "seed"])

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()
        
    def test_meal_index(self):
        response = self.client.get("/meals/")

        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_add_meal(self):
        response = self.client.post("/meals/", json={
            'title': 'Plain Dry Chicken'
        })

        self.assertEqual(response.status_code, 200)

    def test_get_one_meal(self):
        response = self.client.get("/meals/4")

        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, dict)

    def test_update_meal(self):
        response = self.client.put("/meals/4", json={
            'title': 'Sweet Potato Wedges'
        })

        self.assertEqual(response.status_code, 200)

    def test_delete_meal(self):
        response = self.client.delete("/meals/4")

        self.assertEqual(response.status_code, 200)