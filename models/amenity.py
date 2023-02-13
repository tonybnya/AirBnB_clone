#!/usr/bin/python3
# amenity.py
# Author: @tonybnya
"""
Definition of the Amenity class.
This class inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Modelize an Amenity.

    Attributes:
        name (str): name of the amenity.
    """

    name = ""
