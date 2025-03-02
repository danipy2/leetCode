class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        pref = 0
        min_pref = 0
        max_pref = 0
        
        # Iterate through the array and update the prefix sum and its min/max.
        for num in nums:
            pref += num
            min_pref = min(min_pref, pref)
            max_pref = max(max_pref, pref)
        
        # The maximum absolute sum is the difference between the maximum and minimum prefix sum.
        return max_pref - min_pref