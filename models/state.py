#!/usr/bin/python3
"""
Module for State class
"""


from models.base_model import BaseModel


class State(BaseModel):
    """defines State class"""

    name = ""

    """initializes instances"""
    def __init__(self, *args, **kwargs):
        if kwargs.get(id) is not None:
            self.__dict__ = kwargs
        else:
            super().__init__()
