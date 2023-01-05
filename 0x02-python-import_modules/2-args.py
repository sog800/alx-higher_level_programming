#!/usr/bin/python3

def arg(args):
    num = len(args) - 1
    if num > 0:
        print("{} arguments:".format(num))
        x = 1
        while x <= num:
            print("{}: {}".format(x, args[x]))
            x += 1
    else:
        print("{} arguments.".format(num))

if __name__ == "__main__":
    import sys

    arg(sys.argv)
