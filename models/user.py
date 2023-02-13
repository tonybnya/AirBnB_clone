#!/usr/bin/python3
# user.py
# Author: @tonybnya
"""
Definition of the User class.
This class inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Modelize an user.

    Attributes:
        email (str): email of the user.
        password (str): password of the user.
        first_name (str): first name of the user.
        last_name (str): last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
