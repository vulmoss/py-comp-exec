#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/11/20 20:44
# @Author   : VulMoss
# @Site     : 
# @File     : half_select.py
# @Software : PyCharm


"""
N个有序整数数列已放在一维数组中，利用二分查找法查找整数m在数组中的位置。若找到，则输出其下标值；反之，则输出“Not be found!”
"""

def half_select(a):
    low = 0
    high = len(a) -1
    k = -1
    for i in a:
        print(i,end= " ")
    print()
    m = int(input("Enter m = :"))
    while low <= high:
        mid= (low+high) //2
        if m<a[mid]:
            high = mid -1
        else:
            if m > a[mid]:
                low = mid +1
            else:
                k = mid
                break
    if k > 0:
        print("m = %d,index = %d" %(m,k))
    else:
        print("Not be found!")