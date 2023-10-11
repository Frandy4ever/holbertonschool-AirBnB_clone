#!/usr/bin/python3
"""New class inherit from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class representing Amenity that inherit from BaseModel
        Attributes:
            name (str): the name of the amenity
        """

    name = ""
