#!/usr/bin/python3
"""
Base class Module
"""
import os
import csv
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save to csv"""
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline='') as csvfile:
            if list_objs is not None:
                writer = csv.writer(csvfile)
                for obj in list_objs:
                    if cls.__name__ == 'Rectangle':
                        writer.writerow([obj.id, obj.width,
                                         obj.height, obj.x, obj.y])
                    elif cls.__name__ == 'Square':
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Load csv file """
        filename = cls.__name__ + '.csv'
        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            list_objs = []
            for row in reader:
                if cls.__name__ == 'Rectangle':
                    dictionary = {'id': int(row[0]), 'width': int(row[1]),
                                  'height': int(row[2]),
                                  'x': int(row[3]), 'y': int(row[4])}
                elif cls.__name__ == 'Square':
                    dictionary = {'id': int(row[0]), 'size': int(row[1]),
                                  'x': int(row[2]), 'y': int(row[3])}
                list_objs.append(cls.create(**dictionary))
        return list_objs
