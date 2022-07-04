#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    Approve_div = []

    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            Approve_div.append(True)
        else:
            Approve_div.append(False)
    return(Approve_div)
