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
        intervals.append((start,len(caps) - 1,caps[start])) #将最后一个区间也加入到intervals中
        if caps[start] == 'F':       #如果start的是F的话，前一次
            forward += 1
        else:
            backward += 1            #start是B的话，后加一次
        if forward < backward:       #如果往后多的话
            flip = 'F'                #要小的 F
        else:
            flip = 'B'                #往后转的小的话 ，就赋值给B
        for t in intervals:           #在intervals这个数组中循环
            if t[2] == flip:          #只有和转的方向相符的才打印输出
                print('People is positions',t[0],'through',t[1],'flip you caps!')


if __name__ == '__main__':
    s = Soultion()
    s.pleaseConform(cap1)
