#!/usr/bin/python3
"""
Class to print list in ascending
order
"""


class MyList(list):
    """
    Inherits list
    """

    def print_sorted(self):
        """
        print in ascending order
        """
        print(sorted(self))
