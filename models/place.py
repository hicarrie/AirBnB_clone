#!/usr/bin/python3
"""
Module for Place class
"""


from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity


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

    def __init__(self, *args, **kwargs):
        """initializes instances"""
        if len(kwargs) > 0:
            self.__dict__ = kwargs
        else:
            super().__init__()
