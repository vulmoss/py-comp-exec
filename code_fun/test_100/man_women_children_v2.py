#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2023/3/30 19:56
# @Author   : VulMoss
# @Site     : 
# @File     : man_women_children_v2.py
# @Software : PyCharm
'''
实际上，在这个问题中，三种人的数量加起来最多为30人，而不是50元。因此，应该有以下两个限制条件：

x + y + z = 30 （a）

3x + 2y + z = 50 （b）

将式（a）代入式（b），可以得到：

3x + 2y + z = 50

3x + 2y + 30 - x - y <= 50

2x + y = 20

因为x、y、z必须是非负整数，所以x的最大取值不能超过10，y的最大取值不能超过20。

因此，x的取值范围是0到10，y的取值范围是0到20。在这个范围内，可以枚举所有可能的x、y、z组合，找到满足条件的解。对于z，可以根据式（b）计算出来。
'''

def find_combination():
    number = 0
    for x in range(0, 11):
        for y in range(0, 21):
            z = 30 - x - y
            if x > 0 and y > 0 and z > 0 and 3 * x + 2 * y + z == 50:
                number += 1
                print("%2d: %2d %2d %2d" % (number, x, y, z))


if __name__ == "__main__":
    print(" Men Women Children")
    find_combination()
