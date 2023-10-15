#!/usr/bin/python3
"""lookup function"""


def lookup(obj):
    """return list of  attributes of an ogject"""
    return list(dir(obj))
