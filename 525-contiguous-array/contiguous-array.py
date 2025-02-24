class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        s = {0:-1}
        t = 0
        maxm = 0
        c1 = 0
        c0 = 0
        for i in range(len(nums)):
            if nums[i]:
                c1+=1
            else:
                c0+=1
            if c1-c0 not in s:
                s[c1-c0] = i
            else:
                maxm = max(maxm,i-s[c1-c0])
        return maxm