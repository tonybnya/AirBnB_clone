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
from models.user import User


class FileStorage:
    """
    Serialization - Deserialization.

    Attributes:
        __file_path (str): private instance attribute representing
                           the path to the JSON file.
        __objects (dict): empty dictionary to store all objects by
                          <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        # with open(FileStorage.__file_path, 'w') as file_obj:
        #     my_dict = {}
        #     for key, obj in FileStorage.__objects.items():
        #         my_dict[key] = obj.to_dict()
        #     json.dump(my_dict, file_obj)
        dict_objects = {}
        for key, value in FileStorage.__objects.items():
            dict_objects[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as file_obj:
            json.dump(dict_objects, file_obj)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        # try:
        #     with open(FileStorage.__file_path) as file_obj:
        #         contents = json.load(file_obj)
        #         for obj in contents.values():
        #             class_name = obj['__class__']
        #             del obj['__class__']
        #             self.new(eval(class_name)(**obj))
        # except FileNotFoundError:
        #     pass
        try:
            with open(FileStorage.__file_path) as file_obj:
                FileStorage.__objects = json.load(file_obj)

            for key, obj in FileStorage.__objects.items():
                class_name, class_id = key.split(".")
                FileStorage.__objects[key] = eval(class_name)(**obj)
        except FileNotFoundError:
            pass
