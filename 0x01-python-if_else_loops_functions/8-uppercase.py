#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for x in str:
        if ord(x) > 96 and ord(x) < 123:
            uppercase_str += chr(ord(x) - 32)
        else:
            uppercase_str += x
    print(uppercase_str.format())
