#!/usr/bin/python3
"""
Module that divides all matrix elements

"""


def matrix_divided(matrix, div):

    """
    Function that divides matrix elements.

    Args:
    matrix (list): list of lists
    div (int/float): Dividing number of float / int
    type.

    Returns:
    list: New Matrix
    """
    if not isinstance(matrix, list) \
            or not all(isinstance(row, list) for row in matrix):
        raise TypeError("""matrix must be a matrix (list of lists)\
                             of integers/floats""")
    if not all(isinstance(elem, (int, float))
               for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists)\
                         of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round((elem / div), 2) for elem in row] for row in matrix]

    return new_matrix
