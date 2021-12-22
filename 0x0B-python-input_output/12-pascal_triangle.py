#!/usr/bin/python3
""" pascal triangle"""


def pascal_triangle(n):
    """print pascal"""
    ls_1 = []
    if n <= 0:
        return ls_1
    for nu in range(0, n):
        if nu == 0:
            ls_1.append([1])
        else:
            ls_2 = []
            len_last = len(ls_1[-1])
            idx = len(ls_1) - 1
            for nu_2 in range(0, len_last):
                if nu_2 == 0:
                    ls_2.append(1)
                if nu_2 == len_last - 1:
                    ls_2.append(1)
                else:
                    ls_2.append(ls_1[idx][nu_2] + ls_1[idx][nu_2 + 1])
            ls_1.append(ls_2)
    return ls_1
