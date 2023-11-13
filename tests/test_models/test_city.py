#!/usr/bin/python3
import unittest
from models.city import City
"""module: user_test"""


class TestCity(unittest.TestCase):
    """Class: TestCity"""
    def setUp(self):
        """instance setup"""
        self.city = City()

    def testattr(self):
        """Testing the attributes of City"""
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "id"))
        self.assertFalse(hasattr(self.city, "updated_at"))
        self.assertFalse(hasattr(self.city, "random_attr"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.__class__.__name__, "City")
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")
        self.city.name = "San Francisco"
        self.state_id = "343r387"
        self.assertEqual(self.city.name, "San Francisco")

    def testmethod(self):
        """Testing the methods of City"""
        self.city.save()
        self.assertTrue(hasattr(self.city, "updated_at"))

    def teststr(self):
        """Testing the str format of City"""
        s = "[{}] ({}) {}".format(self.city.__class__.__name__,
                                  str(self.city.id),
                                  self.city.__dict__)
        self.assertEqual(print(s), print(self.city))

if __name__ == '__main__':
    unittest.main()
