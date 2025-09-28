class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target = abs(target)
        memo = {}
        def dp(s,i):
            if i == len(nums):
                return 1 if s==target else 0 
            if (s,i) not in memo:
                memo[(s,i)] = dp(s+nums[i],i+1) + dp(s-nums[i],i+1) 
            return memo[(s,i)]
        return dp(0,0)