#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/11/19 14:25
# @Author   : VulMoss
# @Site     : 
# @File     : bubble_sort_v1.py
# @Software : PyCharm


"""
对N个整数（数据由键盘输入）进行升序排列。
缺点结尾不能是空格
"""

def bubbleSort(a):# 输入一个数组
    n = len(a) #n是数组的长度
    i = 1
    while i <= n-1: #循环的次数是数组的元素的个数
        j = 0
        while j < n - i: #🙅🏻‍把这个数组看成两部分，前面的和最后一个，每次循环都是把最大的放到最后
            if a[j] > a[j+1]: #前一个大于后一个的话，大的赋值给t
                t = a[j]
                a[j] = a[j+1] #把小的数值往前面放，
                a[j+1] = t #大的数值赋值给后面
            j += 1
        i += 1
    for a1 in a: #取出每一个数值
        print(a1,end= " ")

def resultSort():
    x = input()
    a = x.split(" ") #把输入按照空格赋值给a 此时的a是一个字符的数组
    for i in range(0,len(a)):
        a[i] = int(a[i]) #把字符变成数值
    print("You input the nums are: \n",a)
    print("Sort is :")
    bubbleSort(a)

if __name__ == "__main__":
    print("The code need you input the end not space")
    resultSort()