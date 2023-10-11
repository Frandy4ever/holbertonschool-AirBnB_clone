#!/usr/bin/python3
"""New class inherit from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class representing a city that inherits from BaseModel
        Attributes:
            state_id (str): The state ID to which the city belongs
            name (str): The name of the city
        """

    state_id = ""
    name = ""
