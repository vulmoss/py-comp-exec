#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/7/21 12:38 AM
# @Author   : VulMoss
# @Site     : 
# @File     : v1.py
# @Software : PyCharm

s=[(6,12),(6,7),(7,8),(6,11),(6,10),(7,12),(7,11),(7,9),(7,8),(8,12),(8,11),(9,11),(9,10),(8,10),(11,12),]

def celebrityDensity(schedule,start,end):
    count = [0] * (end + 1) #全部初始化为0
    for i in range(start, end + 1):#i在最开始的时间和最后的时间遍历
        count[i] = 0 #首先赋值为0
        for c in schedule: #c是每一个名人的时间区间
            if c[0] <= i and c[1] >i:#在这个区间里
                count[i] += 1 #i这个索引对应的数值加1
    return count

def bestTimeToParty(schedule):
    start = schedule[0][0] #初始化start列表的第一个元组的第一个
    end = schedule[0][1]
    for c in schedule:#循环列表中的每一个元组
        start = min(c[0],start)#取值所有的时间最开始的
        end = max(c[1],end) #取值所有的时间最后的
    count = celebrityDensity(schedule,start,end)#将数组和最早的开始和最后的结束带入
    maxcount = 0
    for i in range(start,end +1):
        if count[i] >maxcount:
            maxcount += 1
            time = i#将最多的时间的序列值赋为time
    print('Best Time to attend the party is at ',time,'o\'clock',':',maxcount,'celebrities will be attending!')

if __name__ == '__main__':
    bestTimeToParty(s)