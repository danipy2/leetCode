class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        myd = {}
        count = 0
        for i in answers:
            if i in myd:
                myd[i]-=1
                if myd[i]==0:
                    del myd[i]                              
            else:
                if i:
                    myd[i] = i
                count += i+1
        return count
               