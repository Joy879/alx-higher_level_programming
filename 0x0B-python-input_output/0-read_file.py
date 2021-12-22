#!/usr/bin/python3
""" Defining a function that reads a text file and prints it to stdout
"""


def read_file(filename=""):
    """ Function that reads a text file (UTF8) and prints it to stdout
           Args:
                filename(any): name of the file
"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
