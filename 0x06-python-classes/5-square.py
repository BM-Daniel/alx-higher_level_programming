#!/usr/bin/python3

"""
Write a class Square that defines a square by: (based on 4-square.py)

    Public instance method: def my_print(self): that prints in stdout the
    square with the character #:
        if size is equal to 0, print an empty line
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

    def my_print(self):
        area = self.area()

        if self.__size == 0:
            return print()

        for i in range(1, area + 1):
            if i % self.__size == 0 and i != area:
                print("#")
            else:
                print("#", end="")

        print()
