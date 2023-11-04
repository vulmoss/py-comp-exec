#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2023/11/4 13:14
# @Author   : VulMoss
# @Site     : 冒泡排序v1
# @File     : bubble_v1.py
# @Software : PyCharm

def bubble_Sort(a):
    n = len(a)
    i = 1
    while i < n -1:
        j = 0
        while j < n - i:
            if a[j] > a[j + 1]:
                t = a[j]
                a[j] + a[j+1]
                a[j+1] = t
            j += 1
        i += 1
    for a1 in a:
        print(a1,end = " ")

if __name__ == "__main__":
    x = input("please input some str:")
    a = x.split(" ")
    bubble_Sort(a)
