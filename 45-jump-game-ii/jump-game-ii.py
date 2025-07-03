class Solution:
    def jump(self, nums: List[int]) -> int:
        
        i = 0 
        t = 0 
        count = 0
        maxd = 0
        while maxd < len(nums)-1:
            while i <= maxd:
                t = max(t,i+nums[i])
                i+=1
            count+=1
            maxd = t
            
        return count
            
                