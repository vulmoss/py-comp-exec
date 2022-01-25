class Solution:
    def maxSubArray(self, nums):
        maxNum = float('-inf')
        n = len(nums)
        res = 0
        for i in range(n):
            res = 0
            for j in range(i,n):
                res += nums[j]
                maxNum = max(maxNum,res)
        return maxNum

if __name__ == '__main__':
    s = Solution()
    ms = s.maxSubArray
    nums = [-1,2,3,4,-1]
    print(ms(nums))
