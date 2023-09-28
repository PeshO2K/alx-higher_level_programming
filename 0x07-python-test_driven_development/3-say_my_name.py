#!/usr/bin/python3
"""
Module that prints name.
"""


def say_my_name(first_name, last_name=""):

    """
    Function that prints fullname given
    first and last names

    Args:
    first_name (str): First name. Must be string
    last_name (str, optional): Last name. Must be string

    Return: Nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
