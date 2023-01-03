#!/usr/bin/python3

def remove_char_at(st, n):
    x = 0
    for m in st:
        if x == n:
            x += 1
            continue
        print(m, end='')
        x += 1
