#!/usr/bin/python3
"""
This module contains FileStorage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        if obj:
            key = f'{type(obj).__name__}.{obj.id}'
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        temp = self.__objects
        obj_dict = {obj: temp[obj].to_dict() for obj in temp.keys()}
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            f.write(json.dumps(obj_dict))

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                data = json.loads(f.read())
                for key, value in data.items():
                    model_name, model_id = key.split('.')
                    try:
                        self.new(eval(model_name)(**value))
                    except Exception as e:
                        print(e)

        except Exception:
            self.__objects = {}
