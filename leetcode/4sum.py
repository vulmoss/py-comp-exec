class Soultion():
    def findNum(self,nums,target,N,tempList,results):
        if len(nums) < N or N < 2:
            return
        # two-sum
        if N == 2:
            l = 0
            r = len(nums ) - 1
            while l < r:
                if nums[l] + nums[r] == target:#前后双指针得到了结果
                    results.append(tempList +[nums[l],nums[r]])#将结果保存到results中。
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)):
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.findNum(nums[i +1:],target - nums[i],N-1,tempList +[nums[i]],results)
        return

    def fourSum(self,nums,target):
        nums.sort()
        results = []
        self.findNum(nums,target,4,[],results)
        return results
if __name__=='__main__':
    s = Soultion()
    nums = [1,3,5,6,88,4,6,7,3,23,50,-1,-2,-33,-100]
    target = 1
    ok = s.fourSum(nums,target)
    print(ok)


