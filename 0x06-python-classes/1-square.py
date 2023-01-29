#!/usr/bin/python3

"""
Write a class Square that defines a square by: (based on 0-square.py)

    Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module

"""


class Square:
    """ A blueprint of a Square """

    def __init__(self, size):
        """
        Initialize square class

        Args:
            size (int): The length of the square
        """

        self.__size = size
