#!/usr/bin/python3
"""Defining a function that writes in a file"""


def write_file(filename="", text=""):
    """ return len of text"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
    return len(text)
