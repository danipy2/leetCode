class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        nums.append(0)
        memo = [-1]*(len(nums)+2)
        
        if len(memo)>=3:
            memo[2]  = nums[0]+nums[2]
        def dp(n):
            if n<=2:
                return nums[n-1]

            if memo[n]==-1:
                memo[n] = max(dp(n-2),dp(n-3))+ nums[n-1]
            return memo[n]
        return dp(len(nums))
                
        