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
    i = 23 # 11 * 2 +1
    flag = 0 #标志位
    while flag == 0:
        j = 1 #第几次卖
        x = i # 卖鱼前的总数
        while j <= 4 and x >= 11:
            m = (x + 1) % (j + 1)
            if m == 0: # 每次卖出的数量 x/(j+1) + 1/(j+1)
                x -= (x+1)//(j+1) #剩余多少条
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