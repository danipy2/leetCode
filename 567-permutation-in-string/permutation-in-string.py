class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        myd = {}
        if len(s1) > len(s2):
            return False
        l = 0
        for i in range(len(s2)):
            myd[s2[i]] = myd.get(s2[i],0)+1
            if i >= len(s1)-1:
                if myd == counter:
                    return True
                myd[s2[l]] -=1
                if myd[s2[l]] == 0:
                    del myd[s2[l]]
                l += 1
            
        return False