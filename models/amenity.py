#!/usr/bin/python3
"""
Module for Amenity class
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """defines Amenity class"""

    name = ""

    """initializes instances"""
    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            self.__dict__ = kwargs
        else:
            super().__init__()
