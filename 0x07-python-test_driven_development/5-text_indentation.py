#!/usr/bin/python3
"""
Module that changes indentation
"""


def text_indentation(text):

    """
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
    text(str): A sring to indent

    Returns:
    Nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in ".:?":
        text = text.replace(delim, delim + "\n\n")
    lines = text.splitlines(True)
    text = [line.strip(" ") for line in lines]
    text = "".join(text)
    print(text, end="")
