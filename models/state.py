#!/usr/bin/python3
"""
Module for State class
"""


from models.base_model import BaseModel


class State(BaseModel):
    """defines State class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """initializes instances"""
        if len(kwargs) > 0:
            self.__dict__ = kwargs
        else:
            super().__init__()
