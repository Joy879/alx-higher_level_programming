#!/usr/bin/python3
"""A class Square that defines a square
"""


class Square:
    """Creates a class named Square
    """

    def __init__(self, size=0):
        """__init__ method initializes an intance
        Arg:
            size: private instance attribute, size of square
        """

        self.__size = size

    @property
    def size(self):
        """@property getter function size() to access the
            private instance attribute size
        Return:
            return __size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """@size.setter to decorate size() function to assign value to size
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """

        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """public method area() caculates the area of square
        Return:
            return the area of the square
        """

        return self.size**2
