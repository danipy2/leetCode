class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1 if i!="0" else 0 for i in s ]
        def dp(i):
            if i == len(s):
                return 1
            if memo[i]==-1:
                memo[i]+= dp(i+1)+1
                val = int(s[i])
                if i+1 <len(s) and val*10 + int(s[i+1]) <27:
                    memo[i]+= dp(i+2) 
            return memo[i]
        return dp(0)