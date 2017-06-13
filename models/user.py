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

    def __init__(self, *args, **kwargs):
        """initializes instances"""
        if len(kwargs) > 0:
            self.__dict__ = kwargs
        else:
            super().__init__(self)
