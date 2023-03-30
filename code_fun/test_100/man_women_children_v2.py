#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2023/3/30 19:56
# @Author   : VulMoss
# @Site     : 
# @File     : man_women_children_v2.py
# @Software : PyCharm


def find_combination():
    number = 0
    for x in range(0, 11):
        for y in range(0, 21):
            z = 30 - x - y
            if z >= 0 and 3 * x + 2 * y + z == 50:
                number += 1
                print("%2d: %2d %2d %2d" % (number, x, y, z))


if __name__ == "__main__":
    print(" Men Women Children")
    find_combination()
