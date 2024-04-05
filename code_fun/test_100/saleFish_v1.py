#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2024/4/5 20:34
# @Author   : VulMoss
# @Site     : 
# @File     : saleFish_v1.py
# @Software : PyCharm

"""
小明将养的一缸金鱼分5次出售：第1次卖出全部的一半加1/2条；第2次卖出余下的三分之一加1/3条；第3次卖出余下的四分之一加1/4条；
第4次卖出余下的五分之一加1/5条；最后卖出余下的11条。试编程求出原来鱼缸中共有多少条金鱼。
"""

def soleFish():
    i = 23
    flag = 0
    x = 23
    while flag == 0:
        j = 1
        x = i
        while j <= 4 and x >= 11:
            if (x + 1) % (j + 1) == 0:
                x -= (x+1)//(j+1)
            else:
                x = 0
                break
            j += 1
        if j == 5 and x == 11:
            print("Total have %d fish." %i)
            flag = 1
        i += 2

if __name__ == "__main__":
    soleFish()