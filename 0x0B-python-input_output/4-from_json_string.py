#!/usr/bin/python3
"""
Module returns object from
Json
"""
import json


def from_json_string(my_str):
    """
    function returns object from JSON of object
    """
    return json.loads(my_str)
