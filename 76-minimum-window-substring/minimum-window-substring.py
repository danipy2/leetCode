class Solution:
    def minWindow(self, s: str, t: str) -> str:
        myd = Counter(t)
        n = len(myd)
        l = 0
        minm = s+"*"
        for i in range(len(s)):
            if s[i] in myd:
                myd[s[i]] -=1
                if myd[s[i]] == 0:
                    n-=1
            if l:
                if s[l] in myd:
                    myd[s[l]] +=1
                    if myd[s[l]] == 1:
                        n+=1
                l+=1
            while n==0:
                if len(minm) > i-l+1:
                    minm = s[l:i+1]
                if s[l] in myd:
                    myd[s[l]] +=1
                    if myd[s[l]] ==1:
                        n+=1
                l+=1
        return minm if len(s) >= len(minm) else ""

