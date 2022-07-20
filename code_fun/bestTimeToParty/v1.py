#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/7/21 12:38 AM
# @Author   : VulMoss
# @Site     : 
# @File     : v1.py
# @Software : PyCharm

s=[(6,12),(6,7),(7,8),(6,11),(6,10),(7,12),(7,11),(7,9),(7,8),(8,12),(8,11),(9,11),(9,10),(8,10),(11,12),]

def celebrityDensity(schedule,start,end):
    count = [0] * (end + 1)
    for i in range(start, end + 1):
        count[i] = 0
        for c in schedule:
            if c[0] < i and c[1] >i:
                count[i] += 1
    return count

def bestTimeToParty(schedule):
    start = schedule[0][0]
    end = schedule[0][1]
    for c in schedule:
        start = min(c[0],start)
        end = max(c[1],end)
    count = celebrityDensity(schedule,start,end)
    maxcount = 0
    for i in range(start,end +1):
        if count[i] >maxcount:
            maxcount += 1
            time = i
    print('Best Time to attend the party is at ',time,'o\'clock',':',maxcount,'celebrities will be attending!')

if __name__ == '__main__':
    bestTimeToParty(s)