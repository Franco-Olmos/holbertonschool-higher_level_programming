#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)

    if size == 0:
        return (0, "None")
    else:
        first_char = sentence[0]
        return (size, first_char)
