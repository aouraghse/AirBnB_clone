#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place
from models.user import User
"""module: class Review"""


class Review(BaseModel):
    """class: Review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """method: init"""
        super().__init__(self, *args, **kwargs)
