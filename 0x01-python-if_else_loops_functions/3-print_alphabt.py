#!/usr/bin/python3
for alph in range(97, 123):
    if alph != 101 and alph != 113:
        print("{0:c}".format(alph), end='')
