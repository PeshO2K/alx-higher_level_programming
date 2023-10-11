#!/usr/bin/python3
"""
Module to append to file
"""


def append_write(filename="", text=""):
    """
    Function to append to file
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
