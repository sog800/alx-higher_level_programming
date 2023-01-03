#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        if letter != " " and (not letter.isnumeric()):
            letter = ord(letter)
            if letter >= 97 and letter <= 122:
                letter = letter - 32
            letter = chr(letter)
        print("{}".format(letter), end='')
    print("{}".format("\n"), end='')
