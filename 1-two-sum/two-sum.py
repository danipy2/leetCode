class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myd  = {}
        for i in range(len(nums)):
            t = target-nums[i]
            if t in myd:
                return [i,myd[t]]
            myd[nums[i]] = i
    