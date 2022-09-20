#!/usr/bin/python3
"""
A script made of a class that defines a Rectangle

"""
class Rectangle:
	""" Class that defines a rectangle """
	
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
