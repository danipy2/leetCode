class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minm = len(nums)+1
        for i in range(len(nums)):
            while nums[i] > 0 and nums[i]!=i+1 and nums[i] <= len(nums):
                if nums[i] == nums[nums[i]-1]:
                    break
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
        for i in range(len(nums)):
            if nums[i] != i+1:
                minm = i+1
                break
        return minm

