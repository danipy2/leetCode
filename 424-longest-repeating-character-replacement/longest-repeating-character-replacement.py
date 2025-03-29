class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        myd = {}
        l = 0
        total = 0
        for i in range(len(s)):
            if s[i] in myd:
                myd[s[i]] +=1
            else:
                myd[s[i]] =1
            maxm = self.findmax(myd)
            if maxm + k >= i-l+1:
                total = max(total,i-l+1)
            else:
                if myd[s[l]] == 1:
                    del myd[s[l]] 
                else:
                    myd[s[l]] -=1
                l+=1
        return total
    def findmax(self,arr):
        maxm = 0
        for i in arr:
            maxm = max(maxm,arr[i])
        return maxm
    