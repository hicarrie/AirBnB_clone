#!/usr/bin/python3
"""
Module for serializing and deserializing instances and JSON files
"""


import os
import json
from datetime import datetime


class FileStorage:
    """ defines FileStorage class """

    __file_path = "./file.json"
    __objects = {}

    """ defines __objects """
    def all(self):
        return FileStorage.__objects

    """ sets obj in __objects with key/value pair """
    def new(self, obj):
        name = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[name] = obj

    """ serializes __objects to the JSON file """
    def save(self):
        full_dict = {}
        for i in FileStorage.__objects.keys():
            full_dict[i] = FileStorage.__objects[i].to_json()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            f.write(json.dumps(full_dict))

    """ deserializes the JSON file to __objects """
    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        reload_dict = {"BaseModel": BaseModel, "User": User,"State": State,"City": City, "Amenity": Amenity, "Place": Place, "Review": Review}

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
                temp_reload = json.load(f)
                for obj, value in temp_reload.items():
                    item_class = temp_reload[obj].get("__class__")
                    if item_class in reload_dict:
                        class_func = reload_dict.get(item_class)
                        FileStorage.__objects[obj] = class_func(**temp_reload[obj])
