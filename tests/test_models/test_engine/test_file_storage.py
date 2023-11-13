#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
"""test_file_torage module """


class TestFileStorage(unittest.TestCase):
    """Class: TestFileStorage"""
    def setUp(self):
        """Setting up the instance(s)"""
        self.filestorage = FileStorage()

    def test_attrs(self):
        """testing the attributes of FileStorage"""
        self.assertFalse(hasattr(self.filestorage, "random_attr"))

if "__main__" == __name__:
    unittest.main()
