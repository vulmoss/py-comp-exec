class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        max_ending_index = maxsum =nums[0]
        for i in range(1,n):
            max_ending_index = max(max_ending_index + nums[i],nums[i])
            maxsum = max(max_ending_index,maxsum)
        return  maxsum


if __name__ == '__main__':
    s = Solution()
    ms = s.maxSubArray
    nums = [-1,2,3,4,-1]
    print(ms(nums))
