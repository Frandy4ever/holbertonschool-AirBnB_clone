#!/usr/bin/python3
"""City Class"""
from models import storage
from models.base_model import BaseModel
from model.engine.file_storage import FileStorage


class City(BaseModel):
    """City Class Model"""
    state_id = ""
    name = ""
