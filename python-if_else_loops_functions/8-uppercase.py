#!/usr/bin/python3
def uppercase(str):
    is_upper: ''
    for c in str:
        if (ord(c) > 96 and ord(c) > 123):
            is_upper += chr(ord(c)-32)
        else:
            newtext+= c
    print('{}'.format(is_upper))
