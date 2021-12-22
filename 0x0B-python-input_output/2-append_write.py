#!/usr/bin/python3
"""append text into a file"""


def append_write(filename="", text=""):
    """return the len of text"""
    with open(filename, mode="a", encoding="utf-8") as myFile:
        myFile.write(text)
    return len(text)
