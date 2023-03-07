#!/usr/bin/python3

""" A blueprint for Base class """


class Base:
    """
    This is the Base class
    It is the base class for all classes in this project

    Attributes:
        __nb_objects (int): Number of times the class has been instantiated
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiate the Base class

        Args:
            id (int): This is the id of the new instance
        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
