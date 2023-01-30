#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/12/2 08:00
# @Author   : VulMoss
# @Site     : 
# @File     : personal_income_tax.py
# @Software : PyCharm


"""
编写一个计算个人所得税的程序，要求输入收入金额后，能够输出应缴的个人所得税。个人所得税征收办法如下：起征点
为2000元。·不超过500元的部分，征收5%。·超过500～2000元的部分，征收10%。·超过2000～5000元的部分，
征收15%。·超过5000～20000元的部分，征收20%。·超过20000～40000元的部分，征收25%。
·超过40000～60000元的部分，征收30%。·超过60000～80000元的部分，征收35%。·超过80000～100000元的
部分，征收40%。·超过100000元以上的，征收45%
"""




taxbase = 2000
taxtable=[(0,500,0.05),
          (500,2000,0.10),
          (2000,5000,0.15),
          (5000,20000,0.20),
          (20000,40000,0.25),
          (40000,60000,0.3),
          (60000,80000,0.35),
          (80000,100000,0.40),
          (100000,100000000,0.45)]

def caculateTax(profit):
    tax = 0.0
    profit -= taxbase
    i = 0
    for i in range(len(taxtable)):
        if (profit > taxtable[i][0]):
            if (profit < taxtable[i][1]):
                tax += (taxtable[i][1] - taxtable[i][0]) * taxtable[i][2]
            else:
                tax += (profit - taxtable[i][0]) * taxtable[i][2]
                profit -= taxtable[i][1]
                if profit < 0:
                    profit = 0
                    print("tax range : %6d_%6d range number is %6.2f  out range %6d" %(taxtable[i][0],taxtable[i][1],tax,profit))
                    return tax
if __name__ == '__main__':
    print("please input personal tax: ",end='')
    profit = int(input())
    tax = caculateTax(profit)
    print("you personal tax is %12.2f" % tax)
