#!/usr/bin/python3

"""
Write the class Rectangle that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """
    Creating a blueprint for the rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiate the rectangle class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x-coordinate of the rectangle
            y (int): y-coordinate of the rectangle
            id (int): the id of the rectangle

        Raises:
            TypeError: If the height or the width is not an int
            TypeError: If the x or the y value is not an int
            ValueError: If the height or the with is less than 0
            ValueError: If the x or the y value is less than 0
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Setter and getter for the rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Setter and getter for the rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Setter and getter for x-coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Setter and getter for y-coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
        A method to return the area value of the rectangle instance
        """
        return self.height * self.width

    def display(self):
        """
        Prints out the rectangle using the character #
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """
        A method to assign an argument to each attribute

        Args:
            *args (ints): New values for attributes
                - 1st argument is the id attribute
                - 2nd argument is the width attribute
                - 3rd argument is the height attribute
                - 4th argument is the x-coordinate attribute
                - 5th argument is the y-coordinate attribute
            **kwargs (dict): New key / value pairs for the attributes
        """

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg

                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg

                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v

                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
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
        """
        Return the print() and str() representation of the square object
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)
