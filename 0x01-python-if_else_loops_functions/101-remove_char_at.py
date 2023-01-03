#!/usr/bin/python3

def remove_char_at(st, n):
    x = 0
    rtn = ''
    for m in st:
        if x == n:
            x += 1
            continue
        rtn += m
        x += 1
    return rtn
