class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        r = 0
        l = 0
        countzero = 0
        size = len(nums)
        maxm = 0
        total = 0
        while r<size:
            total += nums[r]
            if total +k >= r-l+1:
                maxm = max(maxm,r-l+1)             
            else:
                total -=nums[l]
                l+=1
            r+=1
        return maxm