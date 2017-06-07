#!/usr/bin/python3
"""
Module for serializing and deserializing instances and JSON files
"""


import os
import json


class FileStorage:
    """ defines FileStorage class """

    __file_path = "./file.json"
    __objects = {}

    """ defines __objects """
    def all(self):
        return self.__objects

    """ sets obj in __objects with key/value pair """
    def new(self, obj):
        self.__objects = {obj.id: obj}

    """ serializes __objects to the JSON file """
    def save(self):
        full_dict = {}
        with open(self.__file_path, "w+", encoding="UTF-8") as f:
            for i in self.__objects.keys():
                temp = (self.__objects[i]).to_json()
                full_dict[i] = temp
            f.write(json.dumps(full_dict))

    """ deserializes the JSON file to __objects """
    def reload(self):
        try:
            if os.path.isfile(self.__file_path):
                with open(self.__file_path, "r", encoding="UTF-8") as f:
                    temp_reload = (json.load(f))
                    for i in temp_reload.keys():
                        self.__objects[i] = dict(temp_reload[i]) #need to somehow convert 
                        return(self.__objects)
        except Exception as e:
            print (e)
