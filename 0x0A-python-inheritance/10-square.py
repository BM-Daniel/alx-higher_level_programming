#!/usr/bin/python3

""" Write a class Square that inherits from Rectangle (9-rectangle.py) """

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ A blueprint of square class """

    def __init__(self, size):
        """ Instantiation of square object """

        super().integer_validator("size", size)
        super().__init__(size, size)

        self.__size = size
