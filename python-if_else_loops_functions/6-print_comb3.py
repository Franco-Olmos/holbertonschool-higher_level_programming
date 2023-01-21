#!/usr/bin/python3
for num in range(0, 10):
    for num1 in range(0, 10):
        if num == 8 and num1 == 9:
            print('{}{}'.format(num, num1))
        elif num < num1:
            print('{}{}'.format(num, num1), end=', ')
