#!/usr/bin/python3
"""
N Queens problem
"""


import sys

n = int(sys.argv[1])

for z in range(1, n - 1):
    step = z + 1
    tstep = step
    new_list = [list([0, 0]) for i in range(0, n)]
    for x in range(0, n):
        new_list[x] = [x, tstep - 1]
        tstep += step
        if (tstep > n and n % 2 == 0):
            tstep -= n + 1
        elif (tstep > n and n % 2 == 1):
            tstep -= n
    print(new_list)
