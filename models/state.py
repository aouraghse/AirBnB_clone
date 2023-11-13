#!/usr/bin/python3
from models.base_model import BaseModel
"""module: class State"""


class State(BaseModel):
    """class: State"""
    name = ""

    def __init__(self, *args, **kwargs):
        """method: init"""
        super().__init__(self, *args, **kwargs)
