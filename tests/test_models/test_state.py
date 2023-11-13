#!/usr/bin/python3
import unittest
from models.state import State
"""module: user_test"""


class TestState(unittest.TestCase):
    """Class: TestState"""
    def setUp(self):
        """instance setup"""
        self.state = State()

    def testattr(self):
        """Testing the attributes of City"""
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "id"))
        self.assertFalse(hasattr(self.state, "updated_at"))
        self.assertFalse(hasattr(self.state, "random_attr"))
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.__class__.__name__, "State")
        self.assertEqual(self.state.name, "")
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

    def testmethod(self):
        """Testing the methods of State"""
        self.state.save()
        self.assertTrue(hasattr(self.state, "updated_at"))

    def teststr(self):
        """Testing the str format of State"""
        s = "[{}] ({}) {}".format(self.state.__class__.__name__,
                                  str(self.state.id),
                                  self.state.__dict__)
        self.assertEqual(print(s), print(self.state))

if __name__ == '__main__':
    unittest.main()
