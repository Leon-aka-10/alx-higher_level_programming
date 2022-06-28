#!/usr/bin/python3
for nums in range(0, 100):
        if nums != 99:
                print("{0:02d}, ".format(nums), end='')
        else:
                print("{0:02d}".format(nums))
