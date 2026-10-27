class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        di = {}
        for ind,value in enumerate(nums):
            if target-value in di:
                return [ind,di[target-value]]
            di[value] = ind
        







         
