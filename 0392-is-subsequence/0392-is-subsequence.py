class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        if len(s) <1:
            return True
        for i in range(len(t)):
            if t[i] == s[left]:
                left += 1
                if left>=(len(s)):
                    return True

        return False
        
            
            
        