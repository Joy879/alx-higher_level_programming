#!/usr/bin/python3
class Square:
    """Creates a class named Square
    """

    def __init__(self, size=0):
        """__init__ method initializes an instance
        Arg:
            size: private instance attribute, size of square
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """

        self.__size = size
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """area: public instance method
        Return:
            return area of square
        """

        return self.__size**2
