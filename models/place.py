#!/usr/bin/python3
"""New class inherit from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Class representing place that inherits from BaseModel

        Attributes:
            city_id (str): ID of city where the place is located
            user_id (str): ID of user who owns the place
            name (str): the name of the place
            description (str): description of the place
            number_rooms (int): number of rooms
            number_bathrooms (int): number of bathrooms
            max_guest (int): max number of guests
            price_by_night (int): price per night to stay
            latitude (float): the latitude coordinate
            longitude (float): the longitude coordinate
            amenity_ids (list): list of amenity IDs
        """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
