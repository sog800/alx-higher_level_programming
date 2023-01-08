#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    if idx < 0 or idx > len(my_list):
        return my_list
    for n in range(len(my_list)):
        if n == idx:
            del my_list[n]
            break
    return my_list
