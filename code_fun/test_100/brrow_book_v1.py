#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/11/16 09:35
# @Author   : VulMoss
# @Site     : 
# @File     : brrow_book_v1.py
# @Software : PyCharm



"""
小明有5本新书，要借给A、B、C三位小朋友，若每人每次只能借1本，则可以有多少种不同的借法
"""


def borrow_book():
    i = 0
    print("A,B,C three people choose book number is ")
    for a in range(1,6):
        for b in range(1,6):
            for c in range(1,6):
                if a != b and a != c and b != c:
                    print("A:%2d B:%2d C:%2d " %(a,b,c), end=' ')
                    i += 1
                    if i% 4 == 0:
                        print()
    print("total %d borrow book" %i)


if __name__ == "__main__":
    borrow_book()