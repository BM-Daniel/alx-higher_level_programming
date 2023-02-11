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

    def to_json(self):
        """ It retrieves a dictionary representation of a student instance """

        return self.__dict__
