#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/12/17 23:21
# @Author   : VulMoss
# @Site     : 
# @File     : rabbit2mountion.py
# @Software : PyCharm


"""
一只小兔子爬上2米高一次跳跃0.4米然后休息2小时，需要多长时间爬到山上
"""

def rabbit_mount():
    m ,s , h= 2, 0.4, 0
    invernel = m // s
    for i in (0,invernel):#invernel是跳跃到达山顶的次数，当到达山顶的时候就结束了本次旅程
        h += 2
        i += 1
    print("the rabbit %d" %h)

if __name__ == "__main__":
    rabbit_mount()
