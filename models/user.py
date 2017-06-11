#!/usr/bin/python3
"""
Module for class User
"""


from models.base_model import BaseModel


class User(BaseModel):
    """defines User class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    """initializes instances"""
    def __init__(self, *args, **kwargs):
        if kwargs.get(id) is not None:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
