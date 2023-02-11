#!/usr/bin/python3

"""
Write a function that writes a string to a text file (UTF8) and returns the
number of characters written
"""


def write_file(filename="", text=""):
    """
    Write to file function

    Args:
        filename (str): Name of file to be written to
        text (str): Text to be written to file

    Returns:
        Number of characters written to file
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
