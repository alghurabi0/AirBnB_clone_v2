#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        if type(cls) == str:
            cls = eval(cls)
            objs = {}
            for key, value in self.__objects.items():
                if type(value) == cls:
                    objs[key] = value
            return objs

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        kwdict = {x: FileStorage.__objects[x].to_dict() for x in FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(kwdict, f)

    def reload(self):
        """Loads storage dictionary from file"""
        
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = FileStorage.classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
    
    def delete(self, obj=None):
        if obj is None:
            return
        try:
            del FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (KeyError, AttributeError):
            pass