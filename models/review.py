#!/user/bin/python3
"""Review Class"""

class Review(BaseModel):
    """Review Class Model"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
                super().__init__(*args, **args, **kwargs)
                self.place.id = kwargs.get("Place_id", "")
                if self.place_id == "":
                    self.place_id = Place().id
    
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **args, **kwargs)
            self.user.id = kwargs.get("User_id", "")
            if self.user_id == "":
                self.user_id = User().id