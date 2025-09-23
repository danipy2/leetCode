class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo  = [0]*len(nums)
        def dp(i):
            if memo[i]==0:
                memo[i] = 1
                for j in range(i+1,len(nums)):
                    if nums[j] > nums[i]:
                        memo[i] = max(dp(j)+1,memo[i])

            return memo[i]
        maxm = 0
        for i in range(len(nums)):
            maxm = max(maxm,dp(i))
        return  maxm

  

  
