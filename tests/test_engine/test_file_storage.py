#!/usr/bin/python3
"""Unittest for testing FileStorage"""

from contextlib import redirect_stdout
import unittest
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import io
import os
import sys


class storageTest(unittest.TestCase):
    """Testing storage access"""

    def test_save(self):
        """test saving of new obj"""
        model = BaseModel()
        x = model.id
        y = "BaseModel.{}".format(x)
        model.save()
        with open("file.json", 'r', encoding="utf-8") as f:
            data = json.loads(f.read())
        self.assertEqual(y in data.keys(), True)

    def test_newobj(self):
        """test self.__ojects in filestorage"""
        storage = FileStorage()
        model = BaseModel()
        x = model.id
        y = "BaseModel.{}".format(x)
        storage.new(model)
        z = storage.all()
        self.assertEqual(y in z.keys(), True)

    def test_reload(self):
        """if file does not exist"""
        storage = FileStorage()
        os.rename('file.json', 'file2.json')
        storage.reload()
        z = storage.all()
        self.assertEqual(z, {})
        os.rename('file2.json', 'file.json')
    
    def help_test_all(self, classname):
        """Helper tests all() method for classname."""
        storage = FileStorage()
        o = eval(classname)()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertTrue(key in storage.all())

    def test_5_all_base_model(self):
        """Tests all() method for BaseModel."""
        self.help_test_all("BaseModel")

    def test_5_all_user(self):
        """Tests all() method for User."""
        self.help_test_all("User")

    def test_5_all_state(self):
        """Tests all() method for State."""
        self.help_test_all("State")

    def test_5_all_city(self):
        """Tests all() method for City."""
        self.help_test_all("City")

    def test_5_all_amenity(self):
        """Tests all() method for Amenity."""
        self.help_test_all("Amenity")

    def test_5_all_place(self):
        """Tests all() method for Place."""
        self.help_test_all("Place")

    def test_5_all_review(self):
        """Tests all() method for Review."""
        self.help_test_all("Review")
    def test_5_all_no_args(self):
        """Tests all() with no arguments."""
        with self.assertRaises(TypeError) as e:
            FileStorage.all()
        msg = "all() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)
    def test_5_all_excess_args(self):
        """Tests all() with too many arguments."""
        with self.assertRaises(TypeError) as e:
            FileStorage.all(self, 98)
        msg = "all() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)
    def help_test_new(self, classname):
        """Helps tests new() method for classname."""
        storage = FileStorage()
        o = eval(classname)()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        self.assertTrue(key in FileStorage._FileStorage__objects)
        self.assertEqual(FileStorage._FileStorage__objects[key], o)
    def test_5_new_base_model(self):
        """Tests new() method for BaseModel."""
        self.help_test_new("BaseModel")

    def test_5_new_user(self):
        """Tests new() method for User."""
        self.help_test_new("User")

    def test_5_new_state(self):
        """Tests new() method for State."""
        self.help_test_new("State")

    def test_5_new_city(self):
        """Tests new() method for City."""
        self.help_test_new("City")

    def test_5_new_amenity(self):
        """Tests new() method for Amenity."""
        self.help_test_new("Amenity")

    def test_5_new_place(self):
        """Tests new() method for Place."""
        self.help_test_new("Place")

    def test_5_new_review(self):
        """Tests new() method for Review."""
        self.help_test_new("Review")
    def test_5_new_no_args(self):
        """Tests new() with no arguments."""
        storage = FileStorage()
        with self.assertRaises(TypeError) as e:
            storage.new()
        msg = "new() missing 1 required positional argument: 'obj'"
        self.assertEqual(str(e.exception), msg)
    def test_5_new_excess_args(self):
        """Tests new() with too many arguments."""
        storage = FileStorage()
        b = BaseModel()
        with self.assertRaises(TypeError) as e:
            storage.new(b, 98)
        msg = "new() takes 2 positional arguments but 3 were given"
        self.assertEqual(str(e.exception), msg)
    def help_test_save(self, classname):
        """Helps tests save() method for classname."""
        
        os.remove('file.json')
        storage = FileStorage()
        o = eval(classname)()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        storage.save()
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
    def test_5_save_base_model(self):
        """Tests save() method for BaseModel."""
        self.help_test_save("BaseModel")

    def test_5_save_user(self):
        """Tests save() method for User."""
        self.help_test_save("User")

    def test_5_save_state(self):
        """Tests save() method for State."""
        self.help_test_save("State")

    def test_5_save_city(self):
        """Tests save() method for City."""
        self.help_test_save("City")

    def test_5_save_amenity(self):
        """Tests save() method for Amenity."""
        self.help_test_save("Amenity")

    def test_5_save_place(self):
        """Tests save() method for Place."""
        self.help_test_save("Place")

    def test_5_save_review(self):
        """Tests save() method for Review."""
        self.help_test_save("Review")
    def test_5_save_no_args(self):
        """Tests save() with no arguments."""
        with self.assertRaises(TypeError) as e:
            FileStorage.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_save_excess_args(self):
        """Tests save() with too many arguments."""
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 98)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)
    def help_test_reload(self, classname):
        """Helps test reload() method for classname."""
        storage = FileStorage()
        os.remove('file.json')
        storage.reload()
        self.assertEqual(storage.all(), {})
        o = eval(classname)()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        storage.save()
        storage.reload()
        self.assertEqual(o.to_dict(), storage.all()[key].to_dict())
    def test_5_reload_base_model(self):
        """Tests reload() method for BaseModel."""
        self.help_test_reload("BaseModel")

    def test_5_reload_user(self):
        """Tests reload() method for User."""
        self.help_test_reload("User")

    def test_5_reload_state(self):
        """Tests reload() method for State."""
        self.help_test_reload("State")

    def test_5_reload_city(self):
        """Tests reload() method for City."""
        self.help_test_reload("City")

    def test_5_reload_amenity(self):
        """Tests reload() method for Amenity."""
        self.help_test_reload("Amenity")

    def test_5_reload_place(self):
        """Tests reload() method for Place."""
        self.help_test_reload("Place")

    def test_5_reload_review(self):
        """Tests reload() method for Review."""
        self.help_test_reload("Review")
    def help_test_reload_mismatch(self, classname):
        """Helps test reload() method for classname."""
        storage = FileStorage()
        os.remove('file.json')
        storage.reload()
        self.assertEqual(storage.all(), {})
        o = eval(classname)()
        storage.new(o)
        key = "{}.{}".format(type(o).__name__, o.id)
        storage.save()
        o.name = "Laura"
        storage.reload()
        self.assertNotEqual(o.to_dict(), storage.all()[key].to_dict())

    def test_5_reload_mismatch_base_model(self):
        """Tests reload() method mismatch for BaseModel."""
        self.help_test_reload_mismatch("BaseModel")

    def test_5_reload_mismatch_user(self):
        """Tests reload_mismatch() method for User."""
        self.help_test_reload_mismatch("User")

    def test_5_reload_mismatch_state(self):
        """Tests reload_mismatch() method for State."""
        self.help_test_reload_mismatch("State")

    def test_5_reload_mismatch_city(self):
        """Tests reload_mismatch() method for City."""
        self.help_test_reload_mismatch("City")

    def test_5_reload_mismatch_amenity(self):
        """Tests reload_mismatch() method for Amenity."""
        self.help_test_reload_mismatch("Amenity")

    def test_5_reload_mismatch_place(self):
        """Tests reload_mismatch() method for Place."""
        self.help_test_reload_mismatch("Place")

    def test_5_reload_mismatch_review(self):
        """Tests reload_mismatch() method for Review."""
        self.help_test_reload_mismatch("Review")
    
    def test_5_reload_no_args(self):
        """Tests reload() with no arguments."""
        with self.assertRaises(TypeError) as e:
            FileStorage.reload()
        msg = "reload() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_5_reload_excess_args(self):
        """Tests reload() with too many arguments."""
        with self.assertRaises(TypeError) as e:
            FileStorage.reload(self, 98)
        msg = "reload() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)
if __name__ == "__main__":
    unittest.main()
