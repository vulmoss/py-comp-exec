#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/11/24 00:25
# @Author   : VulMoss
# @Site     : 
# @File     : three_color_ball.py
# @Software : PyCharm

"""
一个口袋中放有12个球，已知其中3个是红的，3个是白的，6个是黑的，现从中任取8个，问共有多少种可能的颜色搭配？
"""

def ball():
    print("\t rad \t whate \t block")
    print("+++++++++++++++++++++++++++++++++++++++")
    num = 0
    for r in range(0,4):  #3个红球，所以红球的范围是0到3
        for w in range(0,4):
            if 8 - r - w <=6: #黑色的球是6个，所以黑球的范围是0到6 ,
                num += 1
                print("%2d: %d \t\t %d \t \t %d" %(num, r,w,8-r-w))

if __name__ == "__main__":
    ball()