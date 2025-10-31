class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        def backtrack(ind,val):
            nonlocal total
            if ind == len(nums):
                total += val
                return
            backtrack(ind+1,val^nums[ind])
            backtrack(ind+1,val)
        backtrack(0,0)
        return total

