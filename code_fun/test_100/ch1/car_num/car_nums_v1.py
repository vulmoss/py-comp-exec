#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/11/14 20:14
# @Author   : VulMoss
# @Site     : 
# @File     : car_nums.py
# @Software : PyCharm

"""
一辆卡车违反交通规则，撞人后逃跑。现场有三人目?该事件，但都
没有记住车号，只记下了车号的一些特征。?说：牌照的前两位数字是相
同的；乙说：牌照的后两位数字是相同的，但与前两位不同；丙是数学
家，他说：4位的车号刚好是一个整数的平方。请根据以上线索求出车号。
"""

"""
因为前两位相等，所以设定都是i 两个都是j 1不等于j 
"""
def results_car():
    for i in range(10):
        for j in range(10):
            if i != j:
                k = 1000 * i + 100 *i + 10 * j + j
                for temp in range(10000):
                    if temp * temp == k:
                        print("cat nums is  ",k)

if __name__ == "__main__":
    results_car()