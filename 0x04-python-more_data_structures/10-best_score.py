#!/usr/bin/python3
def best_score(a_dictionary):
    none_dict = None
    empty_dict = {}
    if a_dictionary == none_dict:
        return None
    elif a_dictionary == empty_dict:
        return None
    best = max(a_dictionary, key=a_dictionary.get)
    return best
