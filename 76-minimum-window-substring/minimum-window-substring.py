class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        myd = Counter(t)
        n = len(myd)
        l = 0
        minm = ""
        size = len(s)+1
        for i in range(len(s)):
            right_char = s[i]
            if right_char in myd:
                myd[right_char] -=1
                if myd[right_char] == 0:
                    n-=1
            if l:
                if s[l] in myd:
                    myd[s[l]] +=1
                    if myd[s[l]] == 1:
                        n+=1
                l+=1
            while n==0:
                if size > i-l+1:
                    minm = s[l:i+1]
                    size = i-l+1
                if s[l] in myd:
                    myd[s[l]] +=1
                    if myd[s[l]] ==1:
                        n+=1
                l+=1
        return minm if len(s) >= size else ""

