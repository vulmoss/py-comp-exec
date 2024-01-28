#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2024/1/28 18:33
# @Author   : VulMoss
# @Site     : 
# @File     : 1.py
# @Software : PyCharm

def noConflicts(board,current,qindex,n): # current 列  #qindex 行索引
    for j in range(current):
        if board[qindex][j] == 1: #行是否有索引
            return False
    k = 1
    while qindex - k >= 0 and current -k >=0:
        if board[qindex - k][current - k] == 1: # 对角线1 是否
            return  False
        k += 1
    k = 1
    while qindex + k < n and current - k >= 0:
        if board[qindex + k][current -k] == 1:
            return False
    k += 1
    return True
def FourQueens(n=4):
    board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(n):
        board[i][0] = 1
        for j in range(n):
            board[j][1] = 1
            if noConflicts(board,1,j,n):
                for k in range(n):
                    board[k][2] = 1
                    if noConflicts(board,2,k,n):
                        for m in range(n):
                            board[m][3] = 1
                            if noConflicts(board,3,m,n):
                                print(board)
                            board[m][3] = 0
                    board[k][2] = 0
            board[j][1] =0
        board[i][0] = 0
    return


if __name__ == '__main__':
    a=FourQueens()
    print(a)
