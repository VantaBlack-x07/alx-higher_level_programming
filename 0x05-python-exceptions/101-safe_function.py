#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {:s}".format(str(e)), file=sys.stderr)
        return Nonei
