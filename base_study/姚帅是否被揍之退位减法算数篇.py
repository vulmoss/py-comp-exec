#!/usr/bin/env python3
# encoding: utf-8
#__author__ == vulMoss

import random

l = 0
for i in range(0,10):
    print('这是一个20之内的随机练习')
    a = random.randint(12,20)
    print('a = {0}'.format(a))
    m = a % 10
    b = random.randint(m+1,9)
    print('b = {0}'.format(b))
    m = a - b
    c = int(input("输入你算数的{0} - {1} 的结果 :".format(a,b)))
    if c == m:
        print("你的对的，结果是{0}🌹🌹🌹🌹 :".format(m))
        l += 1
    else :
        print("你要加油哦💪")
print("你答对了{0}道题".format(l))
