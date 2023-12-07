#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    result = 0
    for i in range(len(roman_string)):
        current_value = romans[roman_string[i]]
        if i + 1 < len(roman_string):
            next_value = romans[roman_string[i + 1]]
        else:
            next_value = 0
        if current_value < next_value:
            result -= current_value
        else:
            result += current_value
    return result
