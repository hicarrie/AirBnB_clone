#!/usr/bin/python3

from models.base_model import BaseModel

class Review(BaseModel):
    """defines Review class"""

    """initializes instances"""
    def __init__(self, *args, **kwargs):
        #will be Place.id
        self.place_id = ""
        #will be User.id
        self.user_id = ""
        self.text = ""
       
        if kwargs.get(id) != None:
            self.__dict__ = kwargs
        else:
            super().__init__()
