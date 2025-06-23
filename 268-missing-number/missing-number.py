class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            x = nums[i]
            while x < n and nums[x]!=x:
                nums[x],nums[i]  = nums[i],nums[x]
                x = nums[i]
                
        for i in range(n):
            if nums[i] !=i:
                return i
        return n