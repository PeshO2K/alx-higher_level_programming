#!/usr/bin/python3
"""Module Student"""


class Student:
    """
    Defines a Student by first name, last name and age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list): A list of strings representing attribute names

        Returns:
            dict: A dictionary representation of the Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance

        Args:
            json (dict): A dictionary where keys are attribute
            names and values are attribute values
        """
        for key, value in json.items():
            setattr(self, key, value)
