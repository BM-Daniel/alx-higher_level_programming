#!/usr/bin/python3

"""
Write the class Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A blueprint for the square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiate the square class

        Args:
            size (int): The dimensions of the square
            x (int): The x-coordinate of the square
            y (int): The y-coordinate of the square
            id (int): The id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter and setter for the dimension"""
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.height)
