class Solution:
    def maxSubArray(self, nums):
        return self.helper(nums,0,len(nums) -1)
    def helper(self,nums,l,r):
        if l>r:
            return float('-inf')
        mid = (l+r)//2
        left = self.helper(nums,1,mid-1)
        right = self.helper(nums,mid+1,r)
        left_suffix_max_sum = right_suffix_max_sum = 0
        total = 0
        for i in reversed(range(1,mid)):
            total += nums[i]
            left_suffix_max_sum = max(left_suffix_max_sum,total)
        total = 0
        for i in range(mid+1,r+1):
            total += nums[i]
            right_suffix_max_sum = max(total,right_suffix_max_sum)
        coss_max_sum = left_suffix_max_sum + right_suffix_max_sum + nums[mid]
        return max(coss_max_sum,left,right)


if __name__ == '__main__':
    s = Solution()
    ms = s.maxSubArray
    nums = [-1,2,3,4,-1]
    print(ms(nums))
