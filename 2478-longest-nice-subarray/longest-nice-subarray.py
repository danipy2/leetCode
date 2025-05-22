class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        maxm = 1
        x = 0
        total = 0
        for i in range(len(nums)):
            if nums[i] ^ x != total+nums[i]:
                x ^=nums[l]
                total -= nums[l]
                l +=1
            x ^= nums[i] 
            total += nums[i]
            maxm = max(maxm,i-l+1)
        return maxm