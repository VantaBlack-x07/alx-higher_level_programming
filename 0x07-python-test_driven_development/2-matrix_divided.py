#!/usr/bin/python3
"""matrix_divided function"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix."""
    if (not isinstance(matrix, list)
            or not all(isinstance(row, list) for row in matrix)
            or not all((isinstance(num, int) or isinstance(num, float))
                       for row in matrix for num in row)):
        message = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(message)
    if not all(len(matrix[0]) == len(li) for li in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
