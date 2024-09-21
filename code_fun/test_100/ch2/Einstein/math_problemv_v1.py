#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2023/3/17 23:23
# @Author   : VulMoss
# @Site     : 
# @File     : math_problemv_v1.py.py
# @Software : PyCharm

'''
爱因斯坦出了一道这样的数学题：有一条长阶梯，若每步跨2阶，则最后剩一阶，若每步跨3阶，则最后剩2阶，
若每步跨5阶，则最后剩4阶，若每步跨6阶，则最后剩5阶。只有每次跨7阶，最后才正好一阶不剩。请问在1到n内，有多少个数能满足？
'''

def computing_ladder(n):
    print("in 1-%d mount number is:" %n)
    sum = 0
    for i in range(7,n+1):
        if (i%7==0) and (i%6==5) and (i%5==4) and (i%3==2): #这个数字的特性，符合逻辑的i
            sum += 1                                        #每有一个i sum就加1 计数
            print("%d" %i)
    print("the mount 1 - %d number have  %d" %(n,sum))

if __name__ =="__main__":
    while True:                             #不断的循环，可以输入多次n
        n = int(input("please input n :"))
        computing_ladder(n)
