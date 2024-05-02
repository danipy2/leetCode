class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left = 0
        s = [i for i in s]
        if k > len(s):
            k = len(s)
        i = k-1
        x = 0

        while(i<len(s)):
            y = i
            while(left<i):
                s[i],s[left] = s[left],s[i]
                left += 1
                i -= 1
            if y + 2*k >= len(s) and len(s)-1-y >=k:
                i = len(s)-1
            else:
                y += 2*k
                i = y
            
            x += 2*k
            left = x
            
        return "".join(s)