#!/usr/bin/python3
# place.py
# Author: @tonybnya
"""
Definition of the Place class.
This class inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Modelize a Place.

    Attributes:
        city_id (str): id of the corresponding city.
        user_id (str): id of the corresponding user.
        name (str): name of the place.
        description (str): description of the place.
        number_rooms (int): number of rooms of the place.
        number_bathrooms (int): number of bathrooms of the place.
        max_guest (int): maximum number of guests of the place.
        price_by_night (int): price by night of the place.
        latitude (float): latitude of the place.
        longitude (float): longitude of the place.
        amenity_ids (list): list of amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
