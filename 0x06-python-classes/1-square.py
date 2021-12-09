#!/usr/bin/python3
""" Defining a class Square with a private attribute size
"""


class Square:
    """ Defining the class Square
"""
    def __init__(self, size):
        """ Initializing attribute size
        __init__ method initializes the instance
        arg:
            size(int): private instance attribute
        """
        self.__size = size
