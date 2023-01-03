#!/usr/bin/python3

def fizzbuzz():
    for n in range(1, 1001):
        if n == range(1001)[-1]:
            if n % 3 == 0:
                print("Fizz $", end='')
            elif n % 5 == 0:
                print("Buzz $", end='')
            elif (n % 5 == 0) and (n % 3 == 0):
                print("FizzBuzz $", end)
        else:
            if n % 3 == 0:
                print("Fizz", end=' ')
            elif n % 5 == 0:
                print("Buzz", end=' ')
            elif (n % 5 == 0) and (n % 3 == 0):
                print("FizzBuzz", end=' ')
