#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2023/3/30 19:40
# @Author   : VulMoss
# @Site     : 
# @File     : man_women_children.py
# @Software : PyCharm


'''
有30个人，其中有男人，女人和小孩，他们在同一个地方吃饭，总共花了50元，已知每个男人吃饭需要3元，每个女人吃饭需要2元，每个小孩吃饭需要1元，
请通过python编程求出男人、女人和小孩各种多少人
'''

def s_num():
    number = 0
    for x in range(0,11):
        y = 20 - 2*x
        z = 30 -x -y
        if 3*x + 2*y + z ==50:
            number += 1
            print("%2d:%4d%5d%6d" % (number,x,y,z))

if __name__ == "__main__":
    print("     Men  Women  Children")
    s_num()