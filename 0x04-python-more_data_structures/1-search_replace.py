#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if i is search:
            new_list = new_list + [replace]
        else:
            new_list = new_list + [i]
    return new_list
