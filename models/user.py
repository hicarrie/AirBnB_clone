#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """defines BaseModel class"""

    """initializes instances"""
    def __init__(self, *args, **kwargs):
        if kwargs.get(id) != None:
            self.__dict__ = kwargs
        else:
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
            super().__init__()
