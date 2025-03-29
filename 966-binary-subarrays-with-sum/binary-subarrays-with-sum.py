class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        t1 = 0
        t2 = 0
        t = 0
        l = 0
        for i in range(len(nums)):
            t+=nums[i]
            while t>goal:
                t-=nums[l]
                l+=1
            t1+= i-l+1
        t = 0
        l = 0
        for i in range(len(nums)):
            t += nums[i]
            while t>=goal and l<=i:
                t-=nums[l]
                l+=1
            t2 += i-l+1
        return t1-t2