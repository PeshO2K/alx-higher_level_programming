#!/usr/bin/python3
"""
Module for check if object and
class are exactly the same
"""


def inherits_from(obj, a_class):
    """
    compares class and object
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
