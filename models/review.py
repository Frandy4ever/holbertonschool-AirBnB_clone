#!/usr/bin/python3
"""New class inherit from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing a review that inherit from BaseModel
        Attributes:
            place_id (str): ID of the place associated with
            user_id (str): ID of the user who wrote the review
            text (str): text content of the review
        """

    place_id = ""
    user_id = ""
    text = ""
