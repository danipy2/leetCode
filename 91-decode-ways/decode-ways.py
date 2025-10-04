class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [0]*(len(s)+1)
        if s[-1] !="0":
            memo[-2] = 1
        memo[-1] = 1
        
        for i in range(len(s)-2,-1,-1):
            if s[i]!="0":
                memo[i]  = memo[i+1]
                if int(s[i])*10 +int(s[i+1]) < 27:
                    memo[i] += memo[i+2]
        
        return memo[0]