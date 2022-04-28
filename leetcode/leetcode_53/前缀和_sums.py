class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        maxsum = nums[0]
        minsum = n_sums =0
        for i in range(n):
            n_sums += nums[i]
            maxsum = max(maxsum,n_sums - minsum)#只保留住最大的那个结果，既前缀之和最大的
            minsum = min(n_sums,minsum)#算法的精髓所在，加上了新的元素对应的数值之后，是否比以前更小，
        return maxsum




if __name__ == '__main__':
    s = Solution()
    ms = s.maxSubArray
    nums = [-1,2,3,4,-1]
    print(ms(nums))
'''
0.....i....j.....
最大的数组的排列是从i到j  前缀和：j的前缀和-i的前缀和最大
整体来说就是不断的计算前缀和的差
'''