#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os
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

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        if type(cls) == str:
            cls = eval(cls)
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
        classes = {
                'BaseModel': BaseModel,
                'User': User,
                'Place': Place,
                'Amenity': Amenity,
                'Review': Review,
                'State': State,
                'City': City
                }
        if not os.path.exists(FileStorage.__file_path):
            return

        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = None

                data = json.load(file)

                if data is None:
                    return

                FileStorage.__objects = {
                    key: classes[key.split('.')[0]](**value)
                    for key, value in data.items()}
        except Exception:
            pass

    def delete(self, obj=None):
        if is not None:
            try:
                del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
            except (KeyError, AttributeError):
                pass
