#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not roman_string:
        return 0

    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    prev_value = 0

    for char in roman_string[::-1]:
        value = roman_numerals.get(char, 0)

        if value >= prev_value:
            result += value
        else:
            result -= value

        prev_value = value

    return result
