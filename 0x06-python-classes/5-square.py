#!/usr/bin/python3
"""Define a Square"""
class Square:
    """ A class that defines a square by its size
    """
    def __init__(self, size=0):
        """ Function to initialize the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Function that returns the square are of the object
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ Function to returns the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Function to set the size value of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ Function that prints a # square according
        to the size value
        """
        if not self.__size:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end='')
                print()
