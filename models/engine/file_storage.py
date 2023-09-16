#!/usr/bin/python3
"""Module for FileStorage Engine
"""
from json import dump, load


class FileStorage:
    """FileStorage class used to serialise objects to JSON files
    """
    __file_path = "data.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        # Converting the object to a dictionary
        obj_dict = obj.to_dict()

        # Creating a key to store the object
        key = "{}.{}".format(obj_dict['__class__'], obj_dict['id'])

        # Adding the object to our dictionary of objects
        self.__objects[key] = obj_dict

    def save(self):
        with open(self.__file_path, "w+") as f:
            dump(self.__objects, f)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                return load(f)
        except FileNotFoundError:
            pass
