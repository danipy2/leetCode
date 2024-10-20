class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        count = 0
        maxm = 0
        found = False
        left = 0
        for i in range(1,len(s)):
            if s[i] ==s[i-1]:
                count+=1
            if count==2:
                if i-left > maxm:
                    maxm = i-left
                    found = True
                count = 1
                left = left+1
                while left<=i and (s[left]!=s[left-1]):
                    left = left+1
            elif i == len(s)-1:
                if (i-left)+1>maxm:
                    maxm = (i-left)+1

        if found ==0:
            maxm = len(s)
        return maxm
