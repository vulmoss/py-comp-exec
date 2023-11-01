#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2023/4/3 13:15
# @Author   : VulMoss
# @Site     : 
# @File     : palindromeNumber.py
# @Software : PyCharm

'''
打印所有不超过n（取n<256）的其平方具有对称性质的数（也称回文数）。
数字转换成字符串，字符串正序和倒叙一样的，并且数组长度大于2判断为回文数
'''

def panlindreme(n):
    m = n * n
    num_str = str(m)
    if num_str == num_str[::-1] and len(num_str) >1:
        return True
    else:
        return False



if __name__ == '__main__':
    for i in range(0,256):
        while panlindreme(i):
            print(i)
            i = i + 1
            continue
        else:
            continue


