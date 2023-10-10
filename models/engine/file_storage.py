import json
from models.base_model import BaseModel

class FileStorage:
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self, cls=None):
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
        dictionary = {}
        for x, y in self.__objects.items():
            if type(x) == cls:
                dictionary[k] = x
        return dictionary   