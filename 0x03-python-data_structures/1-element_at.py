#!/usr/bin/python3
def element_at(my_list, idx):
    ln = len(my_list) - 1
    if idx < 0 or idx > ln:
        return None
    for i in my_list:
        i = int(i)
        if i == idx:
            return my_list[i]
