import unittest
from api.views import app 
from api.utilities import errors
from testing_data import product_data,missing_product_data

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)
    def test_product_data(self):
        self.assertFalse(errors(product_data))
    def test_missing_product_data(self):
        self.assertEqual(errors(missing_product_data), True)
    def test_product(self):
        response = self.client.get("/products")
        self.assertEqual(response.status_code, 200)

if __name__ =="__main__":
    unittest.main()
