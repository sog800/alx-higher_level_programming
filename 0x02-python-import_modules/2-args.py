#!/usr/bin/python3

def arg(args):
    num = len(args) - 1
    print("{} arguments".format(num))
    if num > 0:
        x = 1
        while x <= num:
            print("{}: {}".format(x, args[x]))
            x += 1


if __name__ == "__main__":
    import sys

    arg(sys.argv)
