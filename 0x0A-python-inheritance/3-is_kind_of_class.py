#!/usr/bin/python3

"""
Write a function that returns True if the object is an instance of, or if the
object is an instance of a class that inherited from, the specified class ;
otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Verify if object is an instance of the class

    Args:
        obj (any): The object to be tested
        a_class (type): The type to verify with the object

    Returns:
        True if object is exactly an instance of the specified class
        Else False
    """

    if isinstance(obj, a_class):
        return True

    return False
