#!/usr/bin/python3
for alph in reversed(range(97, 123)):
    print("{0:c}".format(alph if (alph % 2 == 0) else (alph - 32)), end='')
