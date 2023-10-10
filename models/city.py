#!/usr/bin/python
""" holds class City"""
import models
from models.base_model import BaseModel, Base
from os import getenv


class City(BaseModel, Base):
    """Representation of city """
    pass

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
