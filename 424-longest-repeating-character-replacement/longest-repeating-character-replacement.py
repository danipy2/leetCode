class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myd = {}
        l = 0
        total = 0
        maxm = 1
        for i in range(len(s)):
            if s[i] in myd:
                myd[s[i]] +=1
                maxm = max(maxm,myd[s[i]])
            else:
                myd[s[i]] =1
            if maxm + k >= i-l+1:
                total = max(total,i-l+1)
            else:
                if myd[s[l]] == 1:
                    del myd[s[l]] 
                else:
                    myd[s[l]] -=1
                l+=1
        return total
    