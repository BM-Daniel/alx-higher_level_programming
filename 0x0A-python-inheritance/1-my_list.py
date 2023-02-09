#!/usr/bin/python3

"""
Write a class MyList that inherits from list
"""


class MyList(list):
    """ A class that inherits from list """

    def __init__(self):
        """ Initialize object class """

        super().__init__()

    def print_sorted(self):
        """ Prints the sorted list """

        print(sorted(self))
