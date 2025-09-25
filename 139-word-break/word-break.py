class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cond = False
        set1 = set()
        def dp(i):
            nonlocal cond
            if cond:
                return True
            if i==len(s):
                return True
            if i in set1:
                return False
            set1.add(i)
            for j in range(i,len(s)):
                if s[i:j+1] in wordDict:
                    
                    if dp(j+1):
                        
                        cond  =True
                        return True
            
            return False

        
        return dp(0)
