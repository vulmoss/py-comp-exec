class Soultion:
    def isPalindrome(self,nums):
        l = 0
        n = len(nums) -1
        while l < n:
            if nums[l] != nums[n]:
                return False
            l += 1
            n -= 1
        return True

if __name__ == '__main__':
    s = Soultion()
    m = s.isPalindrome
    nums= 'ydsaudfjia'
    print(m(nums))