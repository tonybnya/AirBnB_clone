#!/usr/bin/python3
# base_model.py
# Author: @tonybnya
"""
Base class that defines all the common attributes/methods.
"""
from uuid import uuid4
from datetime import datetime
import models.storage as storage
# import storage
# from models import storage


class BaseModel:
    """Base class for all the other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize the base attributes.

        Attributes:
            *args (tuple): unused, containing all the attributes.
            **kwargs (dict): key/value pairs for all the attributes.
        """
        form = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"], form)
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs["updated_at"], form)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        """Returns the string representation of an instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute 'updated_at'."""
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """Returns dict containing all keys/values of __dict__ of instance."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()

        return my_dict
