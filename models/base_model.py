#!/usr/bin/python3
"""
This module contains the base class that defines all the common attributes/methods.
"""
from datetime import datetime
import uuid


class BaseModel(object):
    """Base class for all the other classes."""

    def __init__(self, id, created_at, updated_at):
        """Initialize the base attributes."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of an instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self, updated_at):
        """Update the public instance attribute 'updated_at'."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()

        return my_dict
