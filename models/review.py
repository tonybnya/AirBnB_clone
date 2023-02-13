#!/usr/bin/python3
# review.py
# Author: @tonybnya
"""
Definition of the Review class.
This class inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Modelize a Review.

    Attributes:
        place_id (str): id of the corresponding place.
        user_id (str): id of the corresponding user.
        text (str): text description for the review.
    """

    place_id = ""
    user_id = ""
    text = ""
