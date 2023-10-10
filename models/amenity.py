#!/usr/bin/python3
<<<<<<< HEAD
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    pass

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
=======
"""Class Amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class Amenity Model"""
    name = ""
>>>>>>> d554b69a90b56cf03619fa98ce009b9cc7313222
