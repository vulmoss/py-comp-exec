#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/11/22 08:52
# @Author   : VulMoss
# @Site     : 
# @File     : num_system_conversion_v1.py
# @Software : PyCharm


"""

给定一个M进制的数x，实现对x向任意一个非M进制的数的转换。


"""


def char_to_num(ch):
    if ch >= '0' and ch <= '9':
        return int(ch)
    else:
        return ord(ch)

def num_to_char(num):
    if num >= 0 and num <=9:
        return str(num)
    else:
        return chr(num)

def source_to_decimal(temp,source):
    decimal_num = 0
    for i in range(len(temp)):
        decimal_num = (decimal_num * source) + char_to_num(temp[i])
        return decimal_num

def decimal_to_source(decimal_num,object):
    decimal = []
    while decimal_num:
        decimal.append(num_to_char(decimal_num % object))
        decimal_num //= object
    return decimal

def output(decimal):
    f = len(decimal) -1
    while f >= 0:
        print(decimal[f],end=' ')
        f -= 1
    print()


