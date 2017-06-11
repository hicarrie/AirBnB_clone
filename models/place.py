#!/usr/bin/python3

from models.base_model import BaseModel

class Place(BaseModel):
    """defines Place class"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""

    """initializes instances"""
    def __init__(self, *args, **kwargs):
        if kwargs.get(id) != None:
            self.__dict__ = kwargs
        else:
            super().__init__()
