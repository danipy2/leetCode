class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        cond = -1
        count = 0
        for i in range(1,len(nums)):
            if (nums[i]-nums[i-1]) * cond >0:
                if i==1:
                    return False
                cond *=-1
                count+=1
            else:
                
                if  count==3 or nums[i]==nums[i-1]:
                    return False
        else:
            return count==2

