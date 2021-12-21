#!/usr/bin/python3
"""Defining the function"""


def lookup(obj):
    """A function that returns the list of available
    attributes and methods of an object
    Returns a list object
    """
    return dir(obj)
