#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2023/1/3 22:07
# @Author   : VulMoss
# @Site     : 
# @File     : isPrime.py
# @Software : PyCharm

def isPrime():
    v1 = int(input("Please input a number,we will analysisthe number is Prime:\n"))
    for i in range(2,v1):
        if v1 % i == 0:
            print("the %d is not prime" %v1)
            break
        else :
            print("%d is prime" %v1)
            break

if __name__ == "__main__":
    isPrime()
