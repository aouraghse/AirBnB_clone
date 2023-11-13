#!/usr/bin/python3
from models.base_model import BaseModel
"""module: class Amenity"""


class Amenity(BaseModel):
    """class: Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """method: init"""
        super().__init__(self, *args, **kwargs)
