#!/usr/bin/python3

from models.base_model import BaseModel

class City(BaseModel):
    """defines City class"""

    """initializes instances"""
    def __init__(self, *args, **kwargs):
        #state_id will be the State.id
        self.state_id = ""
        self.name = ""
        if kwargs.get(id) != None:
            self.__dict__ = kwargs
        else:
            super().__init__()
