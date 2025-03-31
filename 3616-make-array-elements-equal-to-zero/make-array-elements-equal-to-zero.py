class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        nums = list(accumulate(nums))
        count = 0
        if nums[0] == 0:
            if  nums[-1] == 0:
                count += 2
            elif nums[-1] == 1:
                count+=1
        for i in range(1,len(nums)): 
            curr = nums[i] - nums[i-1]
            right = nums[-1]-nums[i]
            left  = nums[i-1]          
            if curr == 0:
                if  left==right:
                    count += 2
                elif abs(left - right) == 1:
                    count+=1
            
        return count