#!/usr/bin/python3

"""
Write a class Square that defines a square by: (based on 1-square.py)

    Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
            size must be an integer, otherwise raise a TypeError exception
            with the message size must be an integer
            if size is less than 0, raise a ValueError exception with the
            message size must be >= 0

    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self): that returns the current square
    area
"""


class Square:
    """ A blueprint for squares """

    def __init__(self, size=0):
        """
        Class initialization

        Args:
            size (int): Length of the square
        """

        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    @property
    def size(self):
        """ Retrieve the value of private size property """
        return self.__size

    @size.setter
    def size(self, value):
        """ Update the value of the private size property """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Calculate the area of the square """
        return pow(self.__size, 2)
