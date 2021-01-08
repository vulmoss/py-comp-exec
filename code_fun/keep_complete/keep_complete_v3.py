#!/usr/bin/env python3
# encoding: utf-8
#__author__ == 'vulMoss'

cap1 = ['B','B','F','B','B','F','B','F','B','F','B','F','F']
cap2 = ['B','F','B','B','B','F','F','B','F','B','F','B']

def pleaseConformInepass(caps):
    caps = caps + [caps[0]] #数组加上数组的首个数值
    for i in range(1,len(caps)):  #在新的数组中循环
        if caps[i] != caps[i -1]: #第一次循环对比前两个是否相同
            if caps[i] != caps[0]: #如果数组的第i个的值 和首个不同
                print('People in positions',i,end = '') #则打印people
            else :
                print(' through', i - 1,'flip you caps!') #相同的话，打印


if __name__ == '__main__':
    pleaseConformInepass(cap1)

