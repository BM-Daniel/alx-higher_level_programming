#!/usr/bin/python3

"""
Write a class MyInt that inherits from int:
"""


class MyInt(int):
    """
    Blueprint for MyInt class
    MyInt has == and != operators inverted
    """

    def __eq__(self, value):
        """ Set == operator to != operator """

        return self.real != value

    def __ne__(self, value):
        """ Set != operator to == operator """

        return self.real == value
