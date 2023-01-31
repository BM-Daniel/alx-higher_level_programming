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

        self.width = width
        self.height = height

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

        self.__height = value

    def area(self):
        """ Find the area of the shape """

        return (self.__width * self.__height)

    def perimeter(self):
        """ Find the perimeter of the shape """

        if (self.__width == 0) or (self.__height == 0):
            return 0

        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """
        Display object in a readable format for user
        Print out the shape using #
        """

        if (self.__width == 0) or (self.__height == 0):
            return ""

        shape = []
        for i in range(self.__height):
            for j in range(self.__width):
                shape.append("#")

            if i != self.__height - 1:
                shape.append("\n")

        return ("".join(shape))

    def __repr__(self):
        """
        Return a string representation of the triangle to be able to recreate
        a new instance
        """

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Message to print when an instance of the shape class is destroyed
        """

        print("Bye rectangle...")
