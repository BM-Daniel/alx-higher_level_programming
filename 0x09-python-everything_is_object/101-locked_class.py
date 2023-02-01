#!/usr/bin/python3

""" Blueprint for a locked class """

class LockedClass:
    """
    Allow user to instantiate an attribute only if it has name as 'first_name'
    """

    __slots__ - ["First_name"]
