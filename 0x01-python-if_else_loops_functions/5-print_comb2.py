#!/usr/bin/python3

for n in range(100):
    if n == range(100)[-1]:
        print("{}".format(n))
        continue
    print("{:02}".format(n), end=', ')
