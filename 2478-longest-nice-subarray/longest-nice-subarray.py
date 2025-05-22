class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        maxm = 1
        x = 0
        total = 0
        for i in range(len(nums)):
            x ^= nums[i] 
            total += nums[i]
            if x != total:
                x ^=nums[l]
                total -= nums[l]
                l +=1
            maxm = max(maxm,i-l+1)
        return maxm