#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum, weight = 0, 0
    for n in my_list:
        sum = sum + n[0] * n[1]
        weight = weight + n[1]
    return sum / weight
