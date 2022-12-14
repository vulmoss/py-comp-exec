#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/12/14 21:57
# @Author   : VulMoss
# @Site     : 
# @File     : money_max.py
# @Software : PyCharm

"""

假设银行整存整取存款不同期限的月利率为：·0.63%，期限为1年；·0.66%，期限为2年；·0.69%，
期限为3年；·0.75%，期限为5年；·0.84%，期限为8年。现在已知某人手上有2000元，
要求通过计算选择出一种存钱方案，使得这笔钱存入银行20年后获得的利息最多。
假定银行对超出存款期限的那部分时间不付利息

"""





def money_max():
    max = 0.0
    for x8 in range(0,3):
        t5 = (20-8*x8)//5
        for x5 in (0,t5+1):
            t3 = (20-8*x8-5*x5) //3
            for x3 in range(0,t3+1):
                t2 = (20-8*x8-5*x5-3*x3)//2
                for x2 in (0,t2+1):
                    x1 = 20-8*x8-5*x5-3*x3-2*x2
                    result = 2000 * ((1+0.0063*12)**x1) *((1+2*0.0066*12)**x2) *((1+3*0.0069*12)**x3)\
                             *((1+5*0.0075*12)**x5) * ((1+8*0.0084*12)**x8)
                    if result > max:
                        max =result
                        y1 =x1
                        y2=x2
                        y3=x3
                        y5=x5
                        y8=x8
    print("best soultion:")
    print("8 year is %d" %y8)
    print("5 year is %d" % y5)
    print("3 year is %d" % y3)
    print("2 year is %d" % y2)
    print("1 year is %d" % y1)
    print("end the money is %0.2f "%result)

if __name__ =="__main__":
    money_max()