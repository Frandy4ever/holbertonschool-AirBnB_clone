#!/usr/bin/python3
""" Class Place"""

class Place(BaseModel):
    """Class Place Model"""
    city_id = ""
    user_id = ""
    name = ""
    decription = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **args, **kwargs)
        self.city.id = kwargs.get("city_id", "")
        if self.city_id == "":
            self.city_id = City().id

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **args, **kwargs)
        self.user.id = kwargs.get("User_id", "")
        if self.user_id == "":
            self.user_id = User().id

