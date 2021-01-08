#!/usr/bin/env python3
# encoding: utf-8
#__author__ == 'vulMoss'

cap1 = ['F','F','B','B','F','B','F','B','F','B','F','F']
cap2 = ['B','F','B','B','B','F','F','B','F','B','F','B']

class Soultion(object):
    def __int__(self,caps):
        self.caps = caps
    def pleaseConform(self,caps):
        start = forward = backward = 0 #初始化
        intervals = []                 #初始化一个数组
        for i in range(1,len(caps)):    #输入的数组的长度中循环
            if caps[start] != caps[i]:  #数组的start值不等于当前位置的数值
                intervals.append((start,i - 1,caps[start]))  #插入数值start，当前的位置-1，数组中start位置的数值
                if caps[start] == 'F':                       #如果数组中start处的数值是F
                    forward += 1                              #forward的数值+1
                else:
                    backward += 1                              #否则backward+1
                start = i                #数组的start值不等于当前位置的数值的是后，将i赋值给start
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
