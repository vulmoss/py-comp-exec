#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2024/4/4 11:53
# @Author   : VulMoss
# @Site     : 3 color body
# @File     : 3color-body.py
# @Software : vi

"""
total 12 body ,red is 3,white 3,black 6 ,get the 8 , so how many color 
"""

def mayBe():
    print("\t red \t white \t block")
    print("--------------------------")
    num = 0 
    for m in range(0,4):
        for n in range(0,4):
            if 8 -m -n <=6:
                num += 1
                print("%2d: %d \t\t %d \t\t %d" %(num,m,n,8-m-n))

if __name__ == "__main__":
    mayBe()
