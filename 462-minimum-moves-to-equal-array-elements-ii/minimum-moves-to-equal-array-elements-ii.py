class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)
        pre = nums[0]
        minm = total - pre- ((len(nums)-1)*nums[0])
        
        for i in range(1,len(nums)):
            l = (i*nums[i]) -pre 
            r = total - pre -((len(nums)-i-1)*nums[i])-nums[i]
            pre += nums[i]
            minm = min(minm,l+r)
        return minm