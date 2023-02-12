#!/usr/bin/python3
# file_storage.py
# Author: @tonybnya
"""
Adds persistence to all the models created.
This module contains the class FileStorage that serializes to instances
JSON file and deserializes JSON file to instances.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serialization - Deserialization.

    Attributes:
        __file_path (str): private instance attribute representing
                           the path to the JSON file.
        __objects (dict): empty dictionary to store all objects by
                          <class name>.id
    """
    __file_path = "file.json"
    __objects: dict = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj
        # obj_name = obj.__class__.__name__
        # FileStorage.__objects["{}.{}".format(obj_name, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        with open(FileStorage.__file_path, 'a') as file_obj:
            my_dict = {}
            for key, value in FileStorage.__objects.items():
                my_dict[key] = value.to_dict()
            json.dump(my_dict, file_obj)
        # odict = FileStorage.__objects
        # objdict = {obj: odict[obj].to_dict() for obj in odict.key()}
        # with open(FileStorage.__file_path, "w") as file_obj:
        #     json.dump(objdict, file_obj)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path) as file_obj:
                contents = json.load(file_obj)
                for obj in contents.values():
                    class_name = obj['__class__']
                    del obj['__class__']
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
