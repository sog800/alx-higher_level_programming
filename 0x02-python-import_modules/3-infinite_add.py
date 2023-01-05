#!/usr/bin/python3

def add(sumup):
    print(sumup)


if __name__ == '__main__':
    import sys
    ln = len(sys.argv) - 1
    x = 1
    sumup = 0
    while x <= ln:
        sumup += int(sys.argv[x])
        x += 1
    add(sumup)
