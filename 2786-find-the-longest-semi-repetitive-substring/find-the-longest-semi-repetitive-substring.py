class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        count = 0
        maxm = 1
        l = 0
        for i in range(1,len(s)):
            if s[i] ==s[i-1]:
                count+=1
            while(l+1<i) and count>1:
                if s[l] == s[l+1]:
                    count-=1
                l+=1
            else:
                maxm = max(maxm,i-l+1)
        return maxm
