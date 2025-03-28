class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        k = total%p
        if k==0:
            return 0
        myd = {0:-1}
        total = 0
        minm = len(nums)
        for i in range(len(nums)):
            total += nums[i]
            if (p-(k-(total%p) ))%p in myd: 
                minm = min(i-myd[ (p-(k-(total%p) ))%p ],minm)
            myd[total%p] = i
        if minm==len(nums):
            return -1
        return minm

        
