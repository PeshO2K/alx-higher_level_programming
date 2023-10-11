#!/usr/bin/python3
"""Module append after"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containing a specific string.
    """
    new_file = ""
    with open(filename, "r") as f:
        for line in f:
            new_file += line
            if search_string in line:
                new_file += new_string

    with open(filename, "w") as f:
        f.write(new_file)
