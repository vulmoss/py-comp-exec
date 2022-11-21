#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/11/20 20:44
# @Author   : VulMoss
# @Site     : 
# @File     : half_select.py
# @Software : PyCharm


"""
N个有序整数数列已放在一维数组中，利用二分查找法查找整数m在数组中的位置。若找到，则输出其下标值；反之，则输出“Not be found!”
数组是排序好的。
"""

def half_select(a):
    low = 0 #数组最前的
    high = len(a) -1 #在数组的最后面
    k = -1
    for i in a:
        print(i,end= " ")
    print()
    m = int(input("Enter m = : ")) #输入的字符变成数值
    while low <= high:
        mid= (low+high) //2 #mid是中间的那个
        if m<a[mid]: #比中间的小的话
            high = mid -1#高的移动到中间
        else:
            if m > a[mid]:
                low = mid +1
            else:
                k = mid
                break
    if k > 0:
        print("m = %d ,index = %d" %(m,k))
    else:
        print("Not be found!")

if __name__ == "__main__":
    a = [-4,-3,0,4,7,9,13,45]
    half_select(a)
