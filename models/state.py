#!/usr/bin/python3
# state.py
# Author: @tonybnya
"""
Definition of the State class.
This class inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Modelize a State.

    Attributes:
        name (str): name of the state.
    """

    name = ""
