#!/usr/bin/python3
for nums in range(0, 90):
    if nums % 10 > nums / 10:
        if nums != 89:
            print("{0:02d}, ".format(nums), end='')
    else:
            print("{0:02d}".format(nums))
