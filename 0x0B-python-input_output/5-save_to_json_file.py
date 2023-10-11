#!/usr/bin/python3
"""
Module write object to textfile in
Json
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function returns object from JSON of object
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
