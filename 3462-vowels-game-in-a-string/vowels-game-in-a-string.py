class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vow = {"a","e","i","o","u"}
        
        for i in range(len(s)):
            if s[i] in vow:
                return True
        return False
                

            