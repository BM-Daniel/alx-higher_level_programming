#!/usr/bin/python3

"""
Write a function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, attr, value):
    """
    Include new attribute to obj if possible

    Args:
        obj (any): Object to be used
        attr (str): Name of attribute to be added
        value (any): Value assigned to  attribute

    Raises:
        TypeError: if the object can't have new attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
