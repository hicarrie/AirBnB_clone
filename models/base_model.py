#!/usr/bin/python3
"""
Module for base model
"""


from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """ defines BaseModel class """

    timeformat = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """ initializes instance """
        if len(kwargs) > 0:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     self.timeformat)
            if "updated_at" in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                         self.timeformat)
            self.__dict__ = kwargs
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            storage.new(self)

    def save(self):
        """ updates attribute updated_at with current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_json(self):
        """ returns dictionary of all keys/values
        of instance + the class name """
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': str(self.__class__.__name__)})
        for key, value in new_dict.items():
            if isinstance(value, datetime):
                new_dict[key] = value.strftime(self.timeformat)
        return new_dict

    def __str__(self):
        """ prints dictionary of attributes of the instance """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    #def __repr__(self):
        #""" prints dictionary of attributes of the instance """
        #return self.__str__()
