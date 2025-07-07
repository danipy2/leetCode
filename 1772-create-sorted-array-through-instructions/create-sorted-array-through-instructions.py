class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = 10**9 +7
        maxm = max(instructions)
        arr = [0 for i in range(maxm+2)]
        cost = 0

        def findcost(l,r):
            t1 = 0
            t2 = 0
            while l>0:
                t1 += arr[l]
                l -= l & -l
            while r>0:
                t2 += arr[r]
                r -= r & - r
            return t2-t1
        def up(ind):
            while ind<len(arr):
                arr[ind] += 1
                ind += ind & -ind
        for i in instructions:
            cost+= min(findcost(0,i-1),findcost(i,maxm))
            up(i)
        return cost%mod