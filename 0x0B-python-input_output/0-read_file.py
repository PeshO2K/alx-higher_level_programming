#!/usr/bin/python3
"""
Module to read text file
"""


def read_file(filename=""):
    """
    function to read file
    """
    with open(filename, encoding="utf-8",) as file:
        for line in file:
            print(line, end="")
