#!/usr/bin/python3
""" define a class square
"""
class Square:
    """Creates a class named Square
    """

    def __init__(self, size=0):
        """__init__ method intitializes an instance
        Arg:
            size: a private instance attribute, size of square
        """

        self.__size = size

    @property
    def size(self):
        """@property decorates getter function size() to access
            private variable size value
        Return:
            return __size value
        """

        return self.__size

    @size.setter
    def size(self, value):
        """@size.setter decorates setter function size() to set
            private variable size value
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
        Arg:
            size: the size of square
        Return:
            return the area of square
        """

        return self.size**2

    def my_print(self):
        """public method my_print prints the square to the standard output
        """

        if self.size > 0:
            for i in range(self.size):
                print("#"*self.size)
        else:
            print()
