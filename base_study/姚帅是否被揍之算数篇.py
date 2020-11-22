#!/usr/bin/env python3
# encoding: utf-8
#__author__ == vulMoss

import random

print('这是一个20之内的随机练习')
a = random.randint(1,20)
print('a = {0}'.format(a))
b = random.randint(1,a)
print('b = {0}'.format(b))
m = a - b
c = int(input("输入你算数的{0} - {1} 的结果 :".format(a,b)))
if c == m:
    print("你的对的，结果是{0}🌹🌹🌹🌹 :".format(m))
else :
    print("你要加油哦💪")
