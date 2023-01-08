#!/usr/bin/python3
def multiple_returns(sentence):
    ln = len(sentence)
    rtn_tuple = ()
    if ln == 0:
        first_char = None
    else:
        first_char = sentence[0]
    rtn_tuple = ln, first_char
    return rtn_tuple
