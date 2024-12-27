class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            while l<len(s) and s[l].isalnum()==False:
                l+=1
            while r>=0 and s[r].isalnum()==False:
                r-=1
            if l<len(s) and r>=0 and s[r].lower()!=s[l].lower() :
                return False
            l+=1
            r-=1
        return True
