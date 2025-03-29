class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        size = len(nums)
        maxm = 0
        total = 0
        l = 0
        for r in range(len(nums)):
            total += nums[r]
            if total +k >= r-l+1:
                maxm = max(maxm,r-l+1)             
            else:
                total -=nums[l]
                l+=1
        return maxm