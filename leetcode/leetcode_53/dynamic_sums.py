class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        max_ending_index = maxsum =nums[0] #第一个元素初始化
        for i in range(1,n): #从1开始循环
            max_ending_index = max(max_ending_index + nums[i],nums[i]) #临时的最大值判断添加了i的元素的值后 ，时候比i的值大，大的话临时的最大值就给
            maxsum = max(max_ending_index,maxsum)#最大值和临时最大值进行比较。
        return  maxsum


if __name__ == '__main__':
    s = Solution()
    ms = s.maxSubArray
    nums = [-1,2,3,4,-1]
    print(ms(nums))
 '''
 动态规划的思想：Q(list,i)  = max(0,Q(list -1)) + nums[i]
 '''