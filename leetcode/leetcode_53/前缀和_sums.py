class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        maxsum = nums[0]
        minsum = n_sums =0
        for i in range(n):
            n_sums += nums[i]
            maxsum = max(maxsum,n_sums - minsum)
            minsum = min(n_sums,minsum)
        return maxsum




if __name__ == '__main__':
    s = Solution()
    ms = s.maxSubArray
    nums = [-1,2,3,4,-1]
    print(ms(nums))
