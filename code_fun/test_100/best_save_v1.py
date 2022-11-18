#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/11/18 15:44
# @Author   : VulMoss
# @Site     : 
# @File     : best_save_v1.py
# @Software : PyCharm


"""
假设银行一年整存零取的月息为0.63%。现在某人手中有一笔钱，他打算在今后5年中的每年年底取出1000元，到第5年时刚好取完，请算出他存钱时应存入多少。
"""

def best_money():
    i = 0
    money= 0.0
    while i<5:
        money = (money+1000) /(1+0.0063 * 12) #每次都取出1千，所以钱数要加上1千，  被除数是 加上利息之后的百分率
        i += 1
    print("Your sould save money : %0.2f" %money)
if __name__== "__main__":
    best_money()