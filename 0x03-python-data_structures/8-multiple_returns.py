#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        first_character = None
    else:
        first_character = sentence[0]

    length = len(sentence)

    return (length, first_character)
