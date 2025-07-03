class Solution:
    def jump(self, nums: List[int]) -> int:
        
        i = 0 
        t = 0 
        count = 0
        maxd = 0
        while i+1 < len(nums):
            if maxd >= len(nums)-1:
                break
            while i <= maxd:
                t = max(t,i+nums[i])
                i+=1
            count+=1
            maxd = t
            
        return count
            
                