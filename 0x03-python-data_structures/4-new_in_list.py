#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = []
    for i in range(len(my_list)):
        new.append(my_list[i])
    if idx < 0:
        return new
    elif idx >= len(my_list):
        return new
    else:
        new[idx] = element
        return new
