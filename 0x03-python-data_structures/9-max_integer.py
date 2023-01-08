#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    tmp = 0
    for n in my_list:
        n = int(n)
        if n < tmp:
            continue
        else:
            tmp = n
    return tmp
