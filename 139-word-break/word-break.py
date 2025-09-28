class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        set1 = set()
        wordDict = set(wordDict)
        def dp(i):
            if i==len(s):
                return True
            if i in set1:
                return False
            set1.add(i)
            for j in range(i,len(s)):
                if s[i:j+1] in wordDict:
                    if dp(j+1):
                        return True
            
            return False
        return dp(0)
