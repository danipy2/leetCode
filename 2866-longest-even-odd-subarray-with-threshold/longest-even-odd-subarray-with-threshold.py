class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        l = 0
        r = 0 
        maxm = 0
        cond = False
        while r<len(nums):
            while l<len(nums) and (nums[l]%2==1 or nums[l]>threshold):
                l+=1
                r+=1
            r+=1
            while r<len(nums) and nums[r]%2 == (r-l)%2 and nums[r]<=threshold:
                r+=1
            if l <len(nums):
                maxm = max(maxm,r-l)
            l = r
        return maxm
        