class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        r = 0
        l = 0
        countzero = 0
        size = len(nums)
        maxm = 0
        while r<size:
            if nums[r] == 0:
                countzero += 1
            if countzero <= k :
                maxm = max(maxm,r-l+1)
            else:
                if nums[l] == 0:
                    countzero -=1
                l+=1
            r+=1
        return maxm