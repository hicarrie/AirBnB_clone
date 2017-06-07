#!/usr/bin/python3
"""
Module for base model
"""


from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """ defines BaseModel class """

    """ initializes instance """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        storage.new(self)

    """ updates attribute updated_at with current datetime """
    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    """ returns dictionary of all keys/values of instance + the class name """
    def to_json(self):
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': str(self.__class__.__name__)})
        new_dict.update({'created_at': str(self.created_at)})
        new_dict.update({'updated_at': str(self.updated_at)})
        return new_dict

    """ prints dictionary of attributes of the instance """
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
