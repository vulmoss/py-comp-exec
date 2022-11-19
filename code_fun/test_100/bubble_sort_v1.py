#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/11/19 14:25
# @Author   : VulMoss
# @Site     : 
# @File     : bubble_sort_v1.py
# @Software : PyCharm


"""
对N个整数（数据由键盘输入）进行升序排列。
"""

def bubbleSort(a):
    n = len(a)
    i = 1
    while i <= n-1:
        j = 0
        while j < n - i:
            if a[j] > a[j+1]:
                t = a[j]
                a[j] = a[j+1]
                a[j+1] = t
            j += 1
        i += 1
    for a1 in a:
        print(a1,end= " ")

def resultSort():
    x = input()
    a = x.split(" ")
    for i in range(0,len(a)):
        a[i] = int(a[i])
    bubbleSort(a)

if __name__ == "__main__":
    resultSort()