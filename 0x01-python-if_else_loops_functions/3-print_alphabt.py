#!/usr/bin/python3

for n in range(ord('a'), ord('z') + 1):
    if chr(n) == 'q' or chr(n) == 'e':
        continue
    print("{}".format(chr(n)), end='')
