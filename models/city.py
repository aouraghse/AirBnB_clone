#!/usr/bin/python3
from models.base_model import BaseModel
from models.state import State
"""module: class City"""


class City(BaseModel):
    """class: City"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """method: init"""
        super().__init__(self, *args, **kwargs)
