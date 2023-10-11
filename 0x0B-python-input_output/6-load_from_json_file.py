#!/usr/bin/python3
"""
Module write object to textfile in
Json
"""
import json


def load_from_json_file(filename):
    """
    function creates object from JSON file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
