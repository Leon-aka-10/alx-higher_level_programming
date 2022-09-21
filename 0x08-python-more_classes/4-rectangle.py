#!/usr/bin/python3
"""Define a Rectangle"""


class Rectangle:
    """ A class that defines a Rectangle by its size
    """
    def __init__(self, width=0, height=(0, 0)):
        """ Function to initialize the rectangle object
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Function to returns the width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Function to set the width value of the rectangle object
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Function that returns the height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Function that sets the height value of a rectangle object
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Function that calculates rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """ Function that calculates rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def _str_(self):
        """ Function that returns #
        """
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return rectangle
        for x in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Function that returns the cannonical string
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
