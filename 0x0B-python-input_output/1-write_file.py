#!/usr/bin/python3
"""
Module write to file
"""


def write_file(filename="", text=""):
    """
    Function to write to file
    Overwrite contents if it exists
    """
    with open(filename, encoding="utf-8") as file:
        return file.write(text)
