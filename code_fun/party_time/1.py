#!/usr/bin/env python3
# encoding: utf-8
#__author__ == 'vulMoss'

sched = [(6,8),(6,12),(6,7),(7,8),(7,10),(8,9),(8,10),(9,12),(9,10),(10,11),(10,12),(11,12)]

def bestTimeToParty(schedule):
    start = schedule[0][0]
    end = schedule[0][1]
    for c in schedule:
        start = min(c[0],start)
        end = max(c[1],end)

    count = celebrityDensity(schedule,start,end)
    maxcoount = 0
    for i in range(start,end + 1):
        if count[i] > maxcount:
            maxcount = count[i]
            time = i
    print('Best time to attend the party is at', time,'o\'clock',':',maxcount,'celebrities will be attending!')


if __name__ == 'main':
    bestTimeToParty(sched)
