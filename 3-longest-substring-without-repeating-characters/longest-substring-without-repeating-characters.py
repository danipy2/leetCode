class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxm = 0
        myset = set()
        l = 0
        for i in range(len(s)):
            if s[i] in myset:
                while s[l] != s[i]:
                    myset.remove(s[l])   
                    l+=1              
                l+=1
            myset.add(s[i])
            maxm = max(i-l+1,maxm)
        return  maxm