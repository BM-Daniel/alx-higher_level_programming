#!/usr/bin/python3

""" Create a rectangle class """


class Rectangle:
    """ Blueprint of 2D rectangle shape """

    def __init__(self, width=0, height=0):
        """
        Instantiation of objec

        Args:
            width (int): Width of the shape
            height (int): Height of the shape
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Getter for private width property """

        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for private width property """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Getter for private height property """

        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for private height property """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
