#!/usr/bin/python3
"""Unittest for BaseModel"""

from contextlib import redirect_stdout
import unittest
from models.state import State
from datetime import datetime
import io
import os
import sys


class baseTest(unittest.TestCase):
    """Class that tests BaseModel"""

    def test_init(self):
        """test initialisation"""
        model = State()
        model.name = "Test"
        self.assertEqual(model.name, 'Test')

    def test_init2(self):
        """test initialisation"""
        model = State()
        model.name = "Test"
        model.my_number = 29
        self.assertEqual(model.name, "Test")
        self.assertEqual(model.my_number, 29)

    def test_initkwargs(self):
        """test init with kwargs"""
        model = State(name='Test', my_number=30)
        self.assertEqual(model.name, 'Test')
        self.assertEqual(model.my_number, 30)

    def test_initid(self):
        """test allocation of uuid"""
        model = State()
        self.assertEqual(type(model.id), str)
        self.assertEqual(len(model.id), 36)

    def test_initdate(self):
        """test datetime"""
        model = State()
        x = str(datetime.now())[:-10]
        y = str(model.created_at)[:-10]
        z = str(model.updated_at)[:-10]
        self.assertEqual(x, y)

    def test_str(self):
        """test __str__"""
        model = State()
        model.name = "Test"
        model.my_number = 29
        output = ""
        with io.StringIO() as buf, redirect_stdout(buf):
            print(model)
            output = buf.getvalue()
        z = '\'my_number\': 29'
        x = z in output
        self.assertEqual(x, True)

    def test_save(self):
        """test update attr after/during save"""
        model = State()
        x = model.updated_at
        model.name = "Test"
        model.save()
        self.assertNotEqual(x, model.updated_at)
        self.assertEqual(str(x)[:-10], str(model.updated_at)[:-10])

    def test_todict(self):
        """test to_dict object function"""
        model = State()
        x = model.to_dict()
        self.assertEqual('id' in x.keys(), True)
        self.assertEqual('created_at' in x.keys(), True)
        self.assertEqual(type(x.get('created_at')), str)

    def test_todict2(self):
        """test to_dict with new attributes"""
        model = State()
        model.name = "Test"
        x = model.to_dict()
        self.assertEqual('name' in x.keys(), True)
        self.assertEqual('number' in x.keys(), False)
        model.number = 29
        x = model.to_dict()
        self.assertEqual('number' in x.keys(), True)

    def test_modelfromdict(self):
        """test creating basemodel from dict"""
        model = State()
        model.name = "Test"
        x = model.to_dict()
        self.assertEqual('number' in x.keys(), False)
        self.assertEqual('name' in x.keys(), True)
        model2 = State(**x)
        self.assertEqual(model2.name, 'Test')
        self.assertEqual(model2.created_at, model.created_at)


if __name__ == '__main__':
    unittest.main()
    