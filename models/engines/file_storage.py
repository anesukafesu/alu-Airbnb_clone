#!/usr/bin/python3
"""Module for FileStorage Engine
"""
from json import dump, load


class FileStorage:
    """FileStorage class used to serialise objects to JSON files
    """
    __file_path = ""
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj['__class__'], obj['id'])
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, "w") as f:
            dump(f, self.__objects)

    def reload(self):
        try:
            with open(self.__file_path, "r") as f:
                return load(f)
        except FileNotFoundError:
            pass
