#!/usr/bin/python3
"""Base module"""

import json
import os

class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class Initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """To JSON string"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
    
    @classmethod
    def save_to_file(cls, list_objs):
        """Save JSON to file"""
        filename = cls.__name__ + ".json"
        my_list = [obj.to_dictionary() for obj in list_objs]\
        if list_objs else []

        with open(filename, "w") as file:
            file.write(cls.to_json_string(my_list))
    

    @staticmethod
    def from_json_string(json_string):
        """From JSON to dictionary"""
        if json_string:
            return json.loads(json_string)
        else:
            return []
    
    @classmethod
    def create(cls, **dictionary):
        """Create instance"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """Return list of instances"""
        filename = cls.__name__ + ".json"

        if not os.path.exists(filename):
            return []

        with open(filename, "r") as file:
            my_list = cls.from_json_string(file.read())
            return [cls.create(**dict) for dict in my_list]



            
