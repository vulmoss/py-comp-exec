#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/11/15 18:07
# @Author   : VulMoss
# @Site     : 
# @File     : 100chicken.py
# @Software : PyCharm


"""
花100元购买100只鸡 ,公鸡5元一个，母鸡3元一个，小鸡一元3个
"""
def buy_100chicken():
    for cock in range(20):
        for hen in range(33):
            for chicken in range(100):
                if (5 * cock + 3 *hen + chicken / 3 ==100) and (cock + hen + chicken ==100):
                    print("cock=%2d,hen=%2d,chicken=%2d\n" %(cock,hen,chicken))

if __name__ == "__main__":
    buy_100chicken()