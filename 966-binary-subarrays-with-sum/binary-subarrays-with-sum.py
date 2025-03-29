class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        t1 = 0
        t2 = 0
        total1 = 0
        total2 = 0
        l1 = 0
        l2 = 0
        for i in range(len(nums)):
            total1+=nums[i]
            total2+=nums[i]
            while total1>goal:
                total1-=nums[l1]
                l1+=1
            while total2>=goal and l2<=i:
                total2 -= nums[l2]
                l2+=1
            t1+= i-l1+1
            t2+= i-l2+1
        return t1-t2