#!/usr/bin/python3
def roman_to_int(roman_string):
    if not type(roman_string) is str or roman_string is None:
        return 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    rev = roman_string[::-1]
    for i in range(len(rev)):
        if i != 0 and dict[rev[i - 1]] > dict[rev[i]]:
            result = result - dict[rev[i]]
        else:
            result = result + dict[rev[i]]
    return result
