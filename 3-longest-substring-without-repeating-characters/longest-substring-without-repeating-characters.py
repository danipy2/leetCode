class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxm = 0
        myd = {}
        l = 0
        count_rep = 0
        for i in range(len(s)):
            if s[i] in myd:
                myd[s[i]]+=1
                count_rep +=1
            else:
                myd[s[i]] = 1
            if count_rep >=1:
                myd[s[l]]-=1
                if myd[s[l]] == 0:
                    del myd[s[l]]
                else:
                    count_rep-=1             
                l+=1
            else:
                maxm = max(i-l+1,maxm)
        return  maxm