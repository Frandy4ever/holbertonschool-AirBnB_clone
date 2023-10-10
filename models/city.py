<<<<<<< HEAD
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
=======
#!/usr/bin/python3
"""City Class"""
from models import storage
from models.base_model import BaseModel
from model.engine.file_storage import FileStorage


class City(BaseModel):
    """City Class Model"""
    state_id = ""
    name = ""
>>>>>>> d554b69a90b56cf03619fa98ce009b9cc7313222
