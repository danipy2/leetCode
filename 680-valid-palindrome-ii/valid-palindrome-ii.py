class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        ans = True
        def two(l,r,cond):
            count = 0
            while l<r:
                if s[l]!=s[r]:
                    if count:
                        return False
                    count+=1
                    if cond:
                        r-=1
                    else:
                        l+=1
                else:
                    l+=1
                    r-=1
            return True
        if two(l,r,1):
            return True
        return two(l,r,0)
        
        
                