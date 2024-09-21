#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/11/15 08:10
# @Author   : VulMoss
# @Site     : 
# @File     : rabbit_baby_v2.py
# @Software : PyCharm

"""
有一对兔子，从生产后的第三个月看是每个月都生一对兔子🐰，小兔子长到第三个月，每个月又生一对，所有的兔子都不死，30个月内每月的兔子对数
"""

"""
迭代循环，不断用新值取代变量的旧值，然后由变量旧值递推出变量新值的过程  f1 f2  f1 f2 
"""
def fb_number(): #兔子🐰没有伦理问题QAQ
    fb1 = 1
    fb2 = 1
    i = 1
    while i <= 16:
#        print("%6d  %6d" %(fb1,fb2),end = "  ") #输出两个数，一月和二月 
        print("%6d  %6d" %(fb1,fb2)) #输出两个数，一月和二月 
#        if i %4 ==0:
#            print()
        fb1 = fb1 + fb2
        fb2 = fb1 + fb2    
        i += 1
if __name__ == "__main__":
    fb_number()
