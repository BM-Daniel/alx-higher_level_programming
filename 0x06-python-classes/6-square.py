#!/usr/bin/python3

"""
Write a class Square that defines a square by: (based on 5-square.py)

    Public instance method: def my_print(self): that prints in stdout the
    square with the character #:
        if size is equal to 0, print an empty line

    Private instance attribute: position:
        property def position(self): to retrieve it
        property setter def position(self, value): to set it:
            position must be a tuple of 2 positive integers, otherwise raise a
            TypeError exception with the message position must be a tuple of
            2 positive integers
"""


class Square:
    """ A blueprint for squares """

    def __init__(self, size=0, position=(0, 0)):
        """
        Class initialization

        Args:
            size (int): Length of the square
        """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ Retrieve the current position of the square """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ Calculate the area of the square """
        return pow(self.__size, 2)

    def my_print(self):
        """ Print out # """

        if self.__size == 0:
            return print()

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print()
