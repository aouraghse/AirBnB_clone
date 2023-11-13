#!/usr/bin/python3
import unittest
from models.user import User
"""module: user_test"""


class TestUser(unittest.TestCase):
    """Class: TestUser"""
    def setUp(self):
        """instance setup"""
        self.user = User()

    def testattr(self):
        """Testing the attributes of User"""
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "id"))
        self.assertFalse(hasattr(self.user, "updated_at"))
        self.assertFalse(hasattr(self.user, "random_attr"))
        self.assertFalse(hasattr(self.user, "name"))
        self.user.name = "Betty"
        self.user.age = 89
        self.assertTrue(hasattr(self.user, "name"))
        self.assertTrue(hasattr(self.user, "age"))
        delattr(self.user, "name")
        self.assertFalse(hasattr(self.user, "name"))
        self.assertEqual(self.user.__class__.__name__, "User")
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
        self.user.email = "betty@holbertonschool.com"
        self.user.password = "dw82deg6d2dc"
        self.user.first_name = "Betty"
        self.user.last_name = "Holberton"
        self.assertEqual(self.user.email, "betty@holbertonschool.com")
        self.assertEqual(self.user.password, "dw82deg6d2dc")
        self.assertEqual(self.user.first_name, "Betty")
        self.assertEqual(self.user.last_name, "Holberton")

    def testmethod(self):
        """Testing the methods of User"""
        self.user.save()
        self.assertTrue(hasattr(self.user, "updated_at"))

    def teststr(self):
        """Testing the str format of User"""
        s = "[{}] ({}) {}".format(self.user.__class__.__name__,
                                  str(self.user.id),
                                  self.user.__dict__)
        self.assertEqual(print(s), print(self.user))

if __name__ == '__main__':
    unittest.main()
