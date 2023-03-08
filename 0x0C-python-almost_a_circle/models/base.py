#!/usr/bin/python3

""" A blueprint for Base class """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): A list of dictionaries
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This method writes the JSON string representation of list_objs to file

        Args:
            list_objs (list): A list of insatnces who inherit from Base
        """

        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [li.to_dictionary() for li in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string

        Args:
            json_string (str): A string representing a list of dictionaries
        """

        if json_string is None or json_string == "[]":
            return []

        return json.loads(json_string)
