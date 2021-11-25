#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    key = ""
    max = 0
    for i in a_dictionary:
        if int(a_dictionary[i]) > max:
            max = int(a_dictionary[i])
            key = i
