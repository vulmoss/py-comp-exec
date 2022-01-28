class Solution:
    def maxSubArray(self, nums):
        return self.helper(nums,0,len(nums) -1) #调用helper函数，返回最大的
    def helper(self,nums,l,r): #入参3个，nums数组，l左边，r右边
        if l>r:
            return float('-inf') #数组就一个元素，
        mid = (l+r)//2 #中间是左加右 除以2 
        left = self.helper(nums,1,mid-1) #左边的sum是helper函数从1开始到中间-1
        right = self.helper(nums,mid+1,r) #右边是sum 从中间+1开始到r
        left_suffix_max_sum = right_suffix_max_sum = 0 #初始化左集合以及右集合 为0
        total = 0
        for i in reversed(range(1,mid)): #左集合从中间开始向左边
            total += nums[i]
            left_suffix_max_sum = max(left_suffix_max_sum,total)
        total = 0
        for i in range(mid+1,r+1): #右集合从中间+1开始向右到 r+1
            total += nums[i]
            right_suffix_max_sum = max(total,right_suffix_max_sum)
        coss_max_sum = left_suffix_max_sum + right_suffix_max_sum + nums[mid] #加上中间的最大的是 左集合和mid加上右集合
        return max(coss_max_sum,left,right)


if __name__ == '__main__':
    s = Solution()
    ms = s.maxSubArray
    nums = [-1,2,3,4,-1]
    print(ms(nums))