#!/usr/bin/python3
"""
Module for serializing and deserializing instances and JSON files
"""


import os
import json


class FileStorage:
    """ defines FileStorage class """

<<<<<<< HEAD
    __file_path = "file.json"
=======
    __file_path = "./file.json"
>>>>>>> f98c41ab43e917e9a29e244275cd3a74275a7c64
    __objects = {}

    """ defines __objects """
    def all(self):
        return FileStorage.__objects

    """ sets obj in __objects with key/value pair """
    def new(self, obj):
        FileStorage.__objects[obj.id] = obj

    """ serializes __objects to the JSON file """
    def save(self):
        full_dict = {}
        for i in FileStorage.__objects.keys():
            full_dict[i] = FileStorage.__objects[i].to_json()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            f.write(json.dumps(full_dict))

    """ deserializes the JSON file to __objects """
    def reload(self):
<<<<<<< HEAD
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                temp_reload = (json.load(f))
                for i in temp_reload.keys():
                    self.__objects[i] = dict(temp_reload[i]) #need to somehow convert 
                    return(self.__objects)
=======
        from models.base_model import BaseModel
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
                temp_reload = json.load(f)
                for i in temp_reload.keys():
                    FileStorage.__objects[i] = BaseModel(**temp_reload[i])
>>>>>>> f98c41ab43e917e9a29e244275cd3a74275a7c64
