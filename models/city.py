#!/usr/bin/python3
# city.py
# Author: @tonybnya
"""
Definition of the City class.
This class inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Modelize a City.

    Attributes:
        state_id (str): id of the state where city is located.
        name (str): name of the city.
    """

    state_id = ""
    name = ""
