class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min1 = nums[k-1] -  nums[0] 
        for i in range(k,len(nums)):
            if (nums[i] - nums[i-k+1]) < min1:
                min1 = (nums[i] - nums[i-k+1])
        return min1