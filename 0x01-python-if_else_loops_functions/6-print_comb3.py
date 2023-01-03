#!/usr/bin/python3

for n in range(9):
    if n == range(9)[-1]:
        print("{}{}".format(n, range(10)[-1]))
        continue
    for m in range(10):
        if m == 0 or m < n:
            continue
        if m == n:
            continue
        print("{}{}".format(n, m), end=', ')
