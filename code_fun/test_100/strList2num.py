#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2024/10/30 23:38
# @Author   : VulMoss
# @Site     : 
# @File     : strList2num.py
# @Software : PyCharm

def s2n(str_list):
###    str_list = ['0010','0000','0001','1000']
    num_list = [int(item,2) for item in str_list]
    print(num_list)

if __name__ == '__main__':
    str_list = ['0010', '0000', '0001', '1000']
    s2n(str_list)

