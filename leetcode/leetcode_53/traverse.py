class Solution:
    def maxSubArray(self, nums):
        maxNum = float('-inf') #初始化设置为一个无穷小的数字，和谁比都小
        n = len(nums)
        res = 0
        for i in range(n): #第一层循环，主要是固定住数组中的一个元素，
            res = 0
            for j in range(i,n):# 第二层巡检，在固定住第一个元素的时候，遍历数组中的每一个元素
                res += nums[j] #将数组中的元素依次相加
                maxNum = max(maxNum,res) #将大的那个赋值给maxNum
        return maxNum

if __name__ == '__main__':
    s = Solution()
    ms = s.maxSubArray
    nums = [-1,2,3,4,-1]
    print(ms(nums))
