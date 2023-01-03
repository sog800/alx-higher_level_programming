#!/usr/bin/python3

x = 26/2
upper = 90
lower = 122
while x > 0:
    char1 = chr(upper - 1)
    char2 = chr(lower)
    print("{}{}".format(char2, char1), end='')
    upper -= 2
    lower -= 2
    x -= 1
