#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        tmp = my_list[0]
    for n in range(len(my_list)):
        if my_list[n] <= tmp:
            continue
        else:
            tmp = my_list[n]
    return tmp
