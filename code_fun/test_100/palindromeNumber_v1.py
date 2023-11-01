#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2023/4/3 13:15
# @Author   : VulMoss
# @Site     : 
# @File     : palindromeNumber.py
# @Software : PyCharm

'''
打印所有不超过n（取n<256）的其平方具有对称性质的数（也称回文数）。
数字转换成字符串，然后切片的方式，左右取出，并比较 [0:len(num)//2]
'''

def panlindreme(n):
    m = n * n
    num_str = str(m)
    l_num = num_str[0:len(num_str)//2]
    r_num = num_str[len(num_str)//2:]
    if l_num ==r_num[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':
    n = int(input('please input the number: '))
    print(panlindreme(n))
