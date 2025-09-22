class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2:
            return False
        tar = s/2
        memo = {}
        ans = False
        def dp(ind,rem):
            nonlocal ans
            if ans or rem==0:
                ans = True
                return  
            if ind>= len(nums) or rem<0:
                return 
            if (ind+1,rem-nums[ind]) not in memo:
                memo[(ind+1,rem-nums[ind])] = dp(ind+1,rem-nums[ind])
            if (ind+1,rem) not in memo:
                memo[(ind+1,rem)] = dp(ind+1,rem)
        dp(0,tar)
        return ans


