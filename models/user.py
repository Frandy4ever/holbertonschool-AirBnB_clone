#!/usr/bin/python3
"""New class inherit from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class representing a User that inherit from BaseModel

    Attributes:
        email (str): The user's email address
        password (str): The user's password
        first_name (str): the users first name
        last_name (str): the users last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
