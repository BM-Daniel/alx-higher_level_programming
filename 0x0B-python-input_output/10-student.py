#!/usr/bin/python3

""" Write a class Student that defines a student """


class Student:
    """ A blueprint for student class """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation of object

        Args:
            first_name (str): First name of student
            last_name (str): Last name of student
            age (int): Age of student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        It retrieves a dictionary representation of a student instance

        If attrs is a list of strings, only attribute names contained in this
        list must be retrieved.
        Otherwise, all attributes must be retrieved

        Args:
            attrs (list): (optional) The attributes to represent
        """

        if (type(attrs) == list and all(type(item) == str for item in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}

        return self.__dict__
