#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/12/1 08:44
# @Author   : VulMoss
# @Site     : 
# @File     : car_speed.py
# @Software : PyCharm


"""
一辆以固定速度行驶的汽车，司机在上午10点看到里程表上的读数是一个对称数（即这个数从左向右读和从右向
左读是完全一样的），为95859。两小时后里程表上出现了一个新的对称数，该数仍为5位数。问该车的速度是多少？
新的对称数是多少？
"""


def car_speed():
    a = [0,0,0,0,0]
    for i in range(95860,100000): #最小值到6位数字之间循环
        t = 0                    #a的下标
        k = 100000
        while k >= 10:
            m = i % k
            n = k // 10
            a[t] = m //n  # % 取模    // 地板除,整数的除法舍去小数，返回数字序列中，比真正商晓得最接近的数字
            k /= 10
            t += 1
        if a[0] == a[4] and a[1] == a[3]:
            print("the number is : %d%d%d%d%d" %(a[0],a[1],a[2],a[3],a[4]))
            print("the car speed is :%0.2f" %((i-95859)//2.0))
            break


if __name__ == "__main__":
    car_speed()