class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = {}
        nums.sort()
        maxm = 0
        for i in range(len(nums)):
            val = nums[i]
            if val-1 in d:
                maxm = max(i-d[val-1]+1,maxm)
            if val not in d:
                d[val] = i
        return maxm
