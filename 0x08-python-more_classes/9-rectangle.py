#!/usr/bin/python3

""" Create a rectangle class """


class Rectangle:
    """
    Blueprint of 2D rectangle shape

    Attributes:
        number_of_instances (int): The number of instantiated objects
        print_symbol (any): Used as symbol for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Instantiation of objec

        Args:
            width (int): Width of the shape
            height (int): Height of the shape
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Getter for private width property """

        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for private width property """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Getter for private height property """

        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for private height property """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ Find the area of the shape """

        return (self.__width * self.__height)

    def perimeter(self):
        """ Find the perimeter of the shape """

        if (self.__width == 0) or (self.__height == 0):
            return 0

        return ((2 * self.__width) + (2 * self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare the area of both rectangles

        Args:
            rect_1 (Rectangle): Rectangle 1
            rect_2 (Rectangle): Rectangle 2

        Raises:
            TypeError: If one of the parameters is not a Rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Return a rectangle with width = height = size

        Args:
            size (int): The lengths of the rectangle
        """

        return cls(size, size)

    def __str__(self):
        """
        Display object in a readable format for user
        Print out the shape using #
        """

        if (self.__width == 0) or (self.__height == 0):
            return ""

        shape = []
        for i in range(self.__height):
            for j in range(self.__width):
                shape.append(str(self.print_symbol))

            if i != self.__height - 1:
                shape.append("\n")

        return ("".join(shape))

    def __repr__(self):
        """
        Return a string representation of the triangle to be able to recreate
        a new instance
        """

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Message to print when an instance of the shape class is destroyed
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
