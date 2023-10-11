#!/usr/bin/python3
"""Module class to JSON"""
def class_to_json(obj):
    """Function that converts class to JSON"""
    return {key: value for key, value in obj.__dict__.items()
            if type(value) in [list, dict, str, int, bool]}
