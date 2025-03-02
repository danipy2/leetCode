class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        p = [0]
        for i in nums:
            p.append(p[-1]+i)
        l = 0
        k = 0
        maxm = p[1]
        minm = maxm
        print(p)
        for i in range(len(p)):
            if p[i] < p[l]:
                l=i
            if p[i] > p[k]:
                k=i
                
            maxm = max(maxm,p[i]-p[l])
            minm = min(minm,p[i]-p[k])
            print(k,minm)
        return max(abs(minm),maxm)