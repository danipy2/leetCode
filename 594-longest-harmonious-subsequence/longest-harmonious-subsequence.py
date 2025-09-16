class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        maxm = 0
        for i in c:
            if i-1 in c:
                maxm = max(maxm,c[i-1]+c[i])
        return maxm
