class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums[i] *=2
                nums[i+1] = 0
                i+=1
            i+=1
        l = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[l] = nums[l],nums[i]
                l+=1
        return nums
            
                
            
