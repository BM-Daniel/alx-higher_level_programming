#!/usr/bin/python3

"""
Write the class Rectangle that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """
    Creating a blueprint for the rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiate the rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x-coordinate of the rectangle
            y (int): y-coordinate of the rectangle
            id (int): the id of the rectangle

        Raises:
            TypeError: If the height or the width is not an int
            TypeError: If the x or the y value is not an int
            ValueError: If the height or the with is less than 0
            ValueError: If the x or the y value is less than 0
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


    @property
    def width(self):
        """Setter and getter for the rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value


    @property
    def height(self):
        """Setter and getter for the rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value


    @property
    def x(self):
        """Setter and getter for x-coordinate"""
        return self.__x

    @x.setter
    def  x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value


    @property
    def y(self):
        """Setter and getter for y-coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
