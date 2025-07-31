class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        myd = {}
        def findmax(x):
            if x>= len(questions):
                return 0
            val , ind = questions[x]
            curr = x+1 
            if curr+ind not in myd:
                myd[curr+ind] = findmax(ind+curr)
            if curr not in myd:
                myd[curr] = findmax(curr)
            return max(myd[curr+ind]+val,myd[curr])
        return findmax(0)