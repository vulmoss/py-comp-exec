#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2022/11/16 19:07
# @Author   : VulMoss
# @Site     : 
# @File     : fash_or_grid_v1.py
# @Software : PyCharm

"""
中国有句俗语叫“三天打鱼两天晒网”。某人从1990年1月1日起便开始“三天打鱼两天晒网”，问这个人在以后的某一天中是“打鱼”还是“晒网”
"""











def runYear(year): #判断是否为闰年的函数
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        return 1
    else :
        return 0

def countDay(currentDay): #入参是一个字典 {'year':year,'month':month,'day':day}
    perMonth = [0,31,28,31,30,31,30,31,31,30,31,30] #
    totalDay=0
    year = 1990 #从1990开始
    while year < currentDay['year']: #年份大于1990
        if runYear(year) == 1:
            totalDay  = totalDay + 366
        else:
            totalDay = totalDay + 365
        year += 1
    if runYear(currentDay['year']) == 1: #润的话，下面的月份28+1
        perMonth[2] += 1
    i = 0                              #从0开始，算月份的天数
    while i < currentDay['month']:
        totalDay += perMonth[i]
        i += 1
    totalDay += currentDay['day'] #算完月 开始算天数 ----日期没有限制，可以写很大的 例如 32 ，应该根据month的进行判断
    return totalDay               #最后返回的是总的天数

def results_day():
    print("pleae input the year , month,day")
    year,month,day = [int(i) for i in input().split()] #被空格分开的三个数字
    today = {'year':year,'month':month,'day':day}
    totalDay = countDay(today)
    print("%d year%d month%d day - 19900101 %d days" %(year,month,day,totalDay))
    result = totalDay %5
    if result >0 and result <4:
        print("today fash")
    else:
        print("grid")

if __name__ == "__main__":
    results_day()