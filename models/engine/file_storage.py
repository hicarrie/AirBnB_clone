#!/usr/bin/python3
"""
Module for serializing and deserializing instances and JSON files
"""


import os
import json


class FileStorage:
    """ defines FileStorage class """

    __file_path = "../../file.json"
    __objects = {}

    """ defines __objects """
    def all(self):
        return self.__objects

    """ sets obj in __objects with key/value pair """
    def new(self, obj):
        self.__objects = {obj.id: obj}

    """ serializes __objects to the JSON file """
    def save(self):
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            f.write(json.dumps(self.__objects))

    """ deserializes the JSON file to __objects """
    def reload(self):
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, encoding="UTF-8") as f:
                return json.load(f)
