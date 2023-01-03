#!/usr/bin/python3

def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))


for character in range_char("a", "z"):
    print(character, end='')
