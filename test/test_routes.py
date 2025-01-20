import unittest
from app import app

class TestProductRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_list_all_products(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)

    def test_create_product(self):
        data = {"name": "NewProduct", "category": "NewCategory", "price": 49.99, "availability": True}
        response = self.client.post('/products', json=data)
        self.assertEqual(response.status_code, 201)

    def test_update_product(self):
        data = {"name": "UpdatedProduct"}
        response = self.client.put('/products/1', json=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_product(self):
        response = self.client.delete('/products/1')
        self.assertEqual(response.status_code, 204)

    def test_search_by_name(self):
        response = self.client.get('/products?name=NewProduct')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
