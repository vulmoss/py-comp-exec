#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2023/4/2 13:59
# @Author   : VulMoss
# @Site     : 
# @File     : exchange_money.py
# @Software : PyCharm


''''
将5元的人民币兑换成1元、5角和1角的硬币，共有多少种不同的兑换方法。
x/y/z
'''

def exchangeMoney():
    number = 0
    for x in range(0,51,10):
        for y in range(0,51-x,5):
            for z in range(0,51-x-y):
                if x + y + z == 50:
                    number += 1
                    print("%2d: %2d %2d %2d" % (number, x//10, y//5, z))

if __name__ == "__main__":
    print(" the plan is ")
    exchangeMoney()
 
