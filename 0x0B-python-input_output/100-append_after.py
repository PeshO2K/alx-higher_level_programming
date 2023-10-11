#!/usr/bin/python3
"""Module append after"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to file, after each line
    containing a specific string
    """
    with open(filename, 'r+') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines[i] = line + new_string + '\n'
        f.seek(0)
        f.writelines(lines)
