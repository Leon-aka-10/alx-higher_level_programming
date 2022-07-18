#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    element = 0

    for alphnum in range(x):
        try:
            print("{}".format(my_list[alphnum]), end='')
        except TypeError:
            break
        else:
            element += 1

    print()
    return (element)
