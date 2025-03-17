class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0 
        for ones in range(len(nums)):
            if nums[ones]:
                nums[ones],nums[zeros] = nums[zeros],nums[ones]
                zeros+=1
        

            
            
        