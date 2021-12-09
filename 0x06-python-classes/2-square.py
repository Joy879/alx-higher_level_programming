#!/usr/bin/python3
"""A class Square that defines a square
"""


class Square:
    """create a class named Square
    """

    def __init__(self, size=0):
        """__init__ method initializes an instance
        Arg:
            size: private instance attribute
        Raises:
            TypeError: size must be an integer
            ValueError: size must be greater or equal than zero
        """

        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
