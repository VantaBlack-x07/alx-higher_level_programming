#!/usr/bin/python3
def multiple_returns(sentence):
    str_length = len(sentence)
    first_chr = sentence[0] if sentence else None
    
    return str_length, first_chr
