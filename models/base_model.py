#!/usr/bin/python3
"""module: base_model"""
from datetime import datetime
import uuid
import json
from models import storage
ddsp = datetime.strptime


class BaseModel:
    """class BaseModel"""
    dtf = '%Y-%m-%dT%H:%M:%S.%f'
    '''datetime format'''

    def __init__(self, *args, **kwargs):
        """init"""
        if (kwargs.get('id') is not None):
            if "__class__" in kwargs:
                del kwargs["__class__"]
            kwargs['created_at'] = ddsp(kwargs['created_at'], self.dtf)
            if "updated_at" in kwargs:
                kwargs['updated_at'] = ddsp(kwargs['updated_at'], self.dtf)
            self.__dict__ = kwargs
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            storage.new(self)

    def save(self):
        """public instance method: save"""
        """upate time and save object to json file"""
        self.updated_at = datetime.now()
        storage.save()

    def to_json(self):
        """public instance method: to_json """
        new_dict = self.__dict__.copy()
        new_dict.update({'created_at':
                         self.created_at.strftime(self.dtf)})
        new_dict.update({'__class__': str(self.__class__.__name__)})
        if hasattr(self, 'updated_at'):
            new_dict.update({'updated_at':
                             self.updated_at.strftime(self.dtf)})
        return new_dict

    def __str__(self):
        """str overwirte"""
        return "[{}] ({}) {}".format(self.__class__.__name__, str(self.id),
                                     self.__dict__)
