class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        myd = {-1:0}
        maxm = -(inf)
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if i - k in myd:
                maxm = max(total-myd[i-k],maxm)
                myd[i] = min(myd[i-k],total)
            else:
                myd[i] = total
        return maxm
            
            
