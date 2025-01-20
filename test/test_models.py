import unittest
from models import Product

class TestProductModel(unittest.TestCase):
    def setUp(self):
        self.product = Product(name="TestProduct", category="TestCategory", price=99.99, availability=True)
        self.product.save()

    def tearDown(self):
        self.product.delete()

    def test_read_product(self):
        product = Product.find(self.product.id)
        self.assertEqual(product.name, "TestProduct")

    def test_update_product(self):
        self.product.name = "UpdatedProduct"
        self.product.save()
        product = Product.find(self.product.id)
        self.assertEqual(product.name, "UpdatedProduct")

    def test_delete_product(self):
        product_id = self.product.id
        self.product.delete()
        product = Product.find(product_id)
        self.assertIsNone(product)

    def test_list_all_products(self):
        products = Product.all()
        self.assertGreaterEqual(len(products), 1)

    def test_find_by_name(self):
        products = Product.find_by_name("TestProduct")
        self.assertGreaterEqual(len(products), 1)

    def test_find_by_category(self):
        products = Product.find_by_category("TestCategory")
        self.assertGreaterEqual(len(products), 1)

    def test_find_by_availability(self):
        products = Product.find_by_availability(True)
        self.assertGreaterEqual(len(products), 1)

if __name__ == "__main__":
    unittest.main()
