#!/usr/bin/env python3
# encoding: utf-8
#__author__ == 'vulMoss'

cap1 = ['F','F','B','B','F','B','F','B','F','B','F','F']
cap1 = ['B','F','B','B','B','F','F','B','F','B','F','B']

class Soultion(object):
    def __int__(self,caps):
        self.caps = caps
    def pleaseConform(self,caps):
        start = forward = backward = 0
        intervals = []
        for i in range(1,len(caps)):
            if caps[start] != caps[i]:
                intervals.append((start,i - 1,caps[start]))
                if caps[start] == 'F':
                    forward += 1
                else:
                    backward += 1
                start = i
            intervals.append((start,len(caps) - 1,caps[start]))
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            if forward < backward:
                flip = 'F'
            else:
                flip = 'B'
            for t in intervals:
                if t[2] == flip:
                    print('People is positions',t[0],'through',t[1],'flip you caps!')


if __name__ == '__main__':
    s = Soultion()
    s.pleaseConform(cap1)
