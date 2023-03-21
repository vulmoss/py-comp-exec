#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2023/3/18 00:07
# @Author   : VulMoss
# @Site     : 
# @File     : distribution_candy.py.py
# @Software : PyCharm
'''
10个小孩围成一圈分糖果，老师分给第1个小孩10块，第2个小孩2块，第3个小孩8块，第4个小孩22块，第5个小孩16块，第6个小孩4块，第7个小孩10块，
第8个小孩6块，第9个小孩14块，第10个小孩20块。然后所有的小孩同时将手中的糖分一半给右边的小孩；糖块数为奇数的人可向老师要一块。
问经过这样几次后大家手中的糖一样多？每人各有多少块糖？
'''

def judge(candy):
    for i in range(0,10):
        if candy[0] != candy[i]:
            return 1
    return 0

def giveSweet(sweet,j):
    t = [0] * 10
    while (judge(sweet)):
        for i in range(0,10):
            if sweet[i] %2 == 0:
                sweet[i] = sweet[i] //2
                t[i] = sweet[i]
            else:
                sweet[i] = (sweet[i] + 1) //2
                t[i] = sweet[i]
        for n in range(0,9):
            