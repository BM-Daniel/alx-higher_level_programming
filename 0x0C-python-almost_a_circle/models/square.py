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

    def update(self, *args, **kwargs):
        """
        A method to assign an argument to each attribute

        Args:
            *args (ints): New values for attributes
                - 1st argument is the id attribute
                - 2nd argument is the size attribute
                - 3rd argument is the x attribute
                - 4th argument is the y attribute
            **kwargs (dict): New key / value pairs of attributes
        """

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg

                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg

                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v

                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        This method returns the dictionary representation of the object
        """

        return {
                "id": self.id,
                "size": self.height,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.height)
