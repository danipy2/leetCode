class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = Counter(s1)
        myd = {}
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            myd[s2[i]] = myd.get(s2[i],0)+1
        if  myd == counter:
            return True
        l = 0
        for i in range(len(s1),len(s2)):
            myd[s2[l]] -=1
            if myd[s2[l]] == 0:
                del myd[s2[l]]
            myd[s2[i]] = myd.get(s2[i],0)+1
            l += 1
            if myd == counter:
                return True
        return False