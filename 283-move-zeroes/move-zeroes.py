class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 
        right = 1
        while right<len(nums):
            while left < right and nums[left]!=0:
                left+=1
            while right<len(nums) and nums[right]==0:
                right +=1
            if right < len(nums):
                nums[left],nums[right] = nums[right],nums[left]
                right+=1
                left+=1

            
            
        