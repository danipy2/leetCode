class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        acc = list(accumulate(nums,initial=0))
        start = 0
        total = 0
        for i in range(1,len(acc)):
            start = max(0,i-1-nums[i-1])
            total += acc[i]-acc[start]
        return total
