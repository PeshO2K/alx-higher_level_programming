#!/usr/bin/python3
"""
Base class Module
"""
import os
import json


class Base():
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constrctor function
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return JSON rep of dictionaries
        """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write json to file"""
        list_dicts = [obj.to_dictionary() for obj in list_objs]\
            if list_objs else []

        with open(cls.__name__ + '.json', "w") as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """From Json"""
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create preinitialized class"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load from files"""
        filename = cls.__name__ + '.json'
        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as file:
            list_dicts = cls.from_json_string(file.read())

        return [cls.create(**dict_) for dict_ in list_dicts]
