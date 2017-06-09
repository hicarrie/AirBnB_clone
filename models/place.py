#!/usr/bin/python3

from models.base_model import BaseModel

class Place(BaseModel):
    """defines Place class"""

    """initializes instances"""
    def __init__(self, *args, **kwargs):
        #it will be the City.id
        self.city_id = ""
        #it will be the User.id
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        #will be list of Amenity.id later
        self.amenity_ids = ""
        
        if kwargs.get(id) != None:
            self.__dict__ = kwargs
        else:
            super().__init__()
