#!/usr/bin/python3
"""
A script made of a class that defines a Rectangle

"""
class Rectangle:
	""" Class that defines a rectangle """

	number_of_instances = 0
	print_symbol = "#"
	
	def _init_(self, width=0, height=0):
		""" Method that initializes the instance """
		self.width = width
		self.height = height

	@property
	def width(self):
		""" method that returns the value of the width """
		return self._width

	@width.setter
	def width(self, value):
		""" method that defines the width """
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		if value < 0:
		        raise ValueError("width must be >= 0")
		self._width = value

	@property
	def height(self):
		""" method that returns the value of the height """
		return self._height
	
	@height.setter
	def height(self, value):
		""" method that defines the height """
		if not isinstance(value, int):
			raise TypeError("height must be an integer")
		if value < 0:
		        raise ValueError("height must be >= 0")
		self._height = value

	def area(self):
		""" Method that calculates the area of a rectangle """
		return self.width * self.height

	def perimeter(self):
		""" Method that calculates the perimeter of a rectangle """
		if self.width == 0 or self.height == 0:
		   return 0
		return (2 * self.width) + (2 * self.height)
	
	def _str_(self):
		""" Method that returns the Rectangle # """
		rectangle = ""
		if self.width == 0 or self.height == 0:
		   return rectangle

		for x in range(self.height):
		    rectangle += ("#" * self.width) + "\n"

		return rectangle[:-1]

	def __repr__(self):
		""" Method that returns the cannonical string of the instance """
		return "Rectangle({:d}, {:d})".format(self.width, self.height)

	def __del__(self):
		""" Method that prints a message when the instance is deleted """
		Rectangle.number_of_instances -= 1
		print("Bye rectangle...")

	@staticmethod
	def bigger_or_equal(rect_1, rect_2):
		""" Method that returns the bigger Rectangle """
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
		""" Method that returns a new instance of Rectangle class """
		return cls(size, size)
