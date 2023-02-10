#!/usr/bin/python3

"""
Write a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py).
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ A blueprint for rectangle class """

    def __init__(self, width, height):
        """
        Instantiation of class object

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
