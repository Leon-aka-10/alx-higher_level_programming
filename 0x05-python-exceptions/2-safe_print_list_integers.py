#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    element = 0

    for alphnum in range(x):
        try:
            print("{:d}".format(my_list[alphnum]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            element += 1

    print()
    return (element)
