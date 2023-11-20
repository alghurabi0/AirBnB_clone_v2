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
            return FileStorage.__objects
        if type(cls) == str and cls in FileStorage.classes:
            cls = FileStorage.classes[cls]
            objs = {}
            for key, value in FileStorage.__objects.items():
                if type(value) == cls:
                    objs[key] = value
            return objs

    def new(self, obj):
        """Adds new object to storage dictionary"""
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        n = {x: self.__objects[x].to_dict() for x in self.__objects.keys()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(n, f)

    def reload(self):
        """Loads storage dictionary from file"""

        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj is None:
            return
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (KeyError, AttributeError):
            pass
