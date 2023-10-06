#!/usr/bin/python3
"""text_indentation"""


def text_indentation(text):
    """
        prints a text with 2 new lines after each of
        these characters: ., ? :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    printed_s = text.strip().replace('. ', '.\n\n').replace('? ', '?\n\n').replace(': ', ':\n\n')
    print(printed_s, end="")
