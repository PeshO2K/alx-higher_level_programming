#!/usr/bin/python3
"""
Module for check if object and
class are exactly the same
"""


def is_same_class(obj, a_class):
    """
    compares class and object
    """

    return type(obj) is a_class
