#!/usr/bin/python3

from datetime import datetime
import uuid
from models import storage

class BaseModel:
    """
    Base class for all models.

    Attributes:
        id (str): A unique identifier for the object.
        created_at (datetime): The date and time when the object was created.
        updated_at (datetime): The date and time when the object was last updated.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.

        Args:
            *args: Additional arguments (not used).
            **kwargs: Keyword arguments containing object attributes.
        """
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            k_dict = kwargs.copy()
            del k_dict["__class__"]
            for key in k_dict:
                if key in ("created_at", "updated_at"):
                    k_dict[key] = datetime.strptime(k_dict[key], date_format)
            self.__dict__ = k_dict
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A string in the format "[class name] (id) {attributes}".
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the "updated_at" attribute and saves the object to storage.
        """
        self.updated_at = datetime.today()
        storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary representation.

        Returns:
            dict: A dictionary containing the object's attributes.
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
