#!/usr/bin/python3

"""
Write a class BaseGeometry (based on 5-base_geometry.py).
"""


class BaseGeometry():
    """
    A blueprint for the BaseGeometry class
    """

    def area(self):
        """
        Area function of class
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function to validate if value is an integer

        Args:
            name (str): Name of argument
            value (int): Argument to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
