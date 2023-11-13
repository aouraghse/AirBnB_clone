#!/usr/bin/python3
import unittest
from models.review import Review
"""module: review"""


class TestReview(unittest.TestCase):
    """Class: TestReview"""
    def setUp(self):
        """instance setup"""
        self.review = Review()

    def testattr(self):
        """Testing the attributes of Review"""
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "id"))
        self.assertFalse(hasattr(self.review, "updated_at"))
        self.assertFalse(hasattr(self.review, "random_attr"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.__class__.__name__, "Review")
        self.assertEqual(self.review.text, "")

    def testmethod(self):
        """Testing the methods of Review"""
        self.review.save()
        self.assertTrue(hasattr(self.review, "updated_at"))

    def teststr(self):
        """Testing the str format of Review"""
        s = "[{}] ({}) {}".format(self.review.__class__.__name__,
                                  str(self.review.id),
                                  self.review.__dict__)
        self.assertEqual(print(s), print(self.review))

if __name__ == '__main__':
    unittest.main()
