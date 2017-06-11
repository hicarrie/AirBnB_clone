#!/usr/bin/python3
"""
Module for City class
"""


from models.base_model import BaseModel


class City(BaseModel):
    """defines City class"""
    state_id = ""
    name = ""

    """initializes instances"""
    def __init__(self, *args, **kwargs):
        if kwargs.get(id) is not None:
            self.__dict__ = kwargs
        else:
            super().__init__()
