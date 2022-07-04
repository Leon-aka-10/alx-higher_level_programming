#!/usr/bin/python3
def multiple_returns(sentence):
    lsen = len(sentence)

    if lsen == 0:
        new_tuple = (lsen, None)
    else:
        new_tuple = (lsen, sentence[0])

    return(new_tuple)
