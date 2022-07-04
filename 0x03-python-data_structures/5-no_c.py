#!/usr/bin/env python3
def no_c(my_string):
    y = 0

    new_string = my_string[:]

    for x in range(len(my_string)):
        if (my_string[x] == 'c' or my_string[x] == 'C'):
            new_string = new_string[:(x - y)] + my_string[(x + 1):]
           y += 1

    return (new_string)
