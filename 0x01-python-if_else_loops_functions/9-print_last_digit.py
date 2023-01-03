#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        number = int(repr(number)[-1])
    else:
        number = number % 10
    print("{}".format(number), end='')
    return number
