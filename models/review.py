#!/usr/bin/python3
"""
Module for Review class
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """defines Review class"""

    place_id = ""
    user_id = ""
    text = ""

    """initializes instances"""
    def __init__(self, *args, **kwargs):
        if kwargs.get(id) is not None:
            self.__dict__ = kwargs
        else:
            super().__init__()
