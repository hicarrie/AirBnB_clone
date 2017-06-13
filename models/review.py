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

    def __init__(self, *args, **kwargs):
        """initializes instances"""
        if len(kwargs) > 0:
            self.__dict__ = kwargs
        else:
            super().__init__()
