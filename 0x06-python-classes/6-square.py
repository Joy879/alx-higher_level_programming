#!/usr/bin/python3
""" Defining a class square
"""
class Square:
    """Creates a class named Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__ method initializes instance variables
        Args:
            __size: private instance attribute, size of square
            __position: private instance attribute, position of square
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """@property decorates getter function size to access
           private variable size value
        Return:
           return __size value
        """

        return self.__size

    @size.setter
    def size(self, value):
        """@size.setter decorates setter function size to assign
           private variable __size value
        Raises:
           TypeError: size must be an integer
           ValueError: size must be >= 0
        """

        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """@property decorates getter function position to access
           private variable __position value
        Return:
           return __position value
        """

        return self.__position

    @position.setter
    def position(self, value):
        """@position.setter decorates setter function position to assign
           private variable __position value
        Arg:
           value: the value assign to __position
        Raises:
           TypeError: position must be a tuple of 2 positive integers
        """

        if len(value) != 2 or not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """public method area to caculates the area of square
        Return:
           return the area of square
        """

        return self.size**2

    def my_print(self):
        """public method my_print prints the square to the standard output
        """

        if self.size == 0:
            print()
            return
        for j in range(self.position[1]):
            print()
        for i in range(self.size):
            print(' '*self.position[0] + "#"*self.size)
