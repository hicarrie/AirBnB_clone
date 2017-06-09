#!/usr/bin/python3

from models.base_model import BaseModel

class Amenity(BaseModel):
    """defines Amenity class"""

    """initializes instances"""
    def __init__(self, *args, **kwargs):
        self.name = ""

        if kwargs.get(id) != None:
            self.__dict__ = kwargs
        else:
            super().__init__()
