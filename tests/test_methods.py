import unittest
# from api.views import app 
from api.utilities import errors
from testing_data import clean_json,missing_json

class TestMethods(unittest.TestCase):
    def test_clean_json(self):
        self.assertFalse(errors(clean_json))
    def test_missing_json(self):
        self.assertEqual(errors(missing_json), True)

if __name__ =="__main__":
    unittest.main()
