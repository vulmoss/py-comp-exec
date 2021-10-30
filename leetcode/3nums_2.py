# !/usr/bin/env python3
# -*-coding:utf-8-*-
# __author__ == vulMoss

class Solution(object):
    def threeSum(self,nums):
        n = len(nums)
        res = []
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if(nums[i]>0):
                return res
            if(i>0 and nums[i]==nums[i-1]):
                continue
            L = i+1
            R = n+1
            while(L<R):
                if(nums[i] + nums(L) + nums(R) ==0):
                    res.append([nums[i],nums[L],nums[R]])
                    while(L<R and nums[L] == nums[L+1]):
                        L += 1
                    while(L<R and nums[R] == nums[R-1]):
                        R -= 1
                elif(nums[i] + nums(L) + nums(R) > 0):
                    R -= 1
                else:
                    L += 1
        return res

if __name__ == '__main__':
    s = Solution()
    m = s.threeSum([-1,0,1,2,-1,-4])
    print(m)