#!/usr/bin/python3
"""text_indentation function"""


def text_indentation(text):
    """
        prints a text with 2 new lines after each of
        these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    printed_str = text.strip().replace('. ', '.\n\n').replace('? ', '?\n\n').replace(': ', ':\n\n')
    print(printed_str, end="")
