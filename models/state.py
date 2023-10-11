#!/usr/bin/python3
"""New class inherit from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class representing a State that inherit from BaseModel
        Attributes:
            name (str): the name of the state
        """

    name = ""
