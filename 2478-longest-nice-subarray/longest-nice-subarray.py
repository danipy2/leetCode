class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        maxm = 1
        x = nums[0]
        for i in range(1,len(nums)):
            while nums[i] & x:
                x ^=nums[l]
                l +=1
            x |= nums[i] 
            maxm = max(maxm,i-l+1)
        return maxm