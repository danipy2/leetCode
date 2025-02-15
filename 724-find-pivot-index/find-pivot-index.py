class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        p = [0]
        for i in range(len(nums)):
            p.append(p[-1] + nums[i])
        l = 0
        r = len(p)-1
        for i in range(1,len(p)):
            if (p[i]-nums[i-1]) == (p[-1]-p[i] ):
                return i-1
        return -1
