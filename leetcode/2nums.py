# !/usr/bin/env python3
# -*-coding:utf-8-*-
# __author__ == vulMoss

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {} #数组用于和nums进行比对
        for i, num in enumerate(nums): #nums中的每一个数字的序列和数值
            if (target - num) in d: #如果目标的数减去本次在数组中提取出来的数 在d这个数组中存在
                return [d[target -num],i] #结果返回 上一个数字在d数组中的value ， 以及本次的序列值
            d[num] = i # key和value num值为key， 序列为value
if __name__ == '__main__':
    s = Solution()
    l = s.twoSum([5,4,3,4,56],59)
    print(l)