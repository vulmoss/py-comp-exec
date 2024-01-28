#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2024/1/28 18:33
# @Author   : VulMoss
# @Site     : 
# @File     : 1.py
# @Software : PyCharm

def noConflicts(board,current,qindex,n): # current 列 #qindex 行索引
    for j in range(current):
        if board[qindex][j] == 1: #行是否有索引
            return False
    k = 1
    while qindex - k >= 0 and current -k >=0:
        if board[qindex - k][current - k] == 1: # 对角线1 是否
            return  False
        k += 1
    k = 1
    while qindex + k < n and current - k >= 0:
        if board[qindex + k][current -k] == 1:
            return False
        K += 1
    return True
