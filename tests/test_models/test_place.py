#!/usr/bin/python3
import unittest
from models.place import Place
"""module: user_test"""


class TestPlace(unittest.TestCase):
    """Class: TestPlace"""
    def setUp(self):
        """instance setup"""
        self.place = Place()

    def testattr(self):
        """Testing the attributes of Place"""
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertTrue(hasattr(self.place, "id"))
        self.assertFalse(hasattr(self.place, "updated_at"))
        self.assertFalse(hasattr(self.place, "random_attr"))
        self.assertEqual(self.place.__class__.__name__, "Place")
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def testmethod(self):
        """Testing the methods of City"""
        self.place.save()
        self.assertTrue(hasattr(self.place, "updated_at"))

    def teststr(self):
        """Testing the str format of Place"""
        s = "[{}] ({}) {}".format(self.place.__class__.__name__,
                                  str(self.place.id),
                                  self.place.__dict__)
        self.assertEqual(print(s), print(self.place))

if __name__ == '__main__':
    unittest.main()
