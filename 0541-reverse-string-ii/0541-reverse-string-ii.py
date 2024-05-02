class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        left = 0
        if k > len(s):
            k = len(s)
        i = k-1
        x = 0

        while(i<len(s)):
            y = i
            tempo = s[left:i+1]
            tempo = tempo[::-1]
            s = s[:left] + tempo + s[i+1:]
            if y + 2*k >= len(s) and len(s)-1-y >=k:
                i = len(s)-1
            else:
                y += 2*k
                i = y
            
            x += 2*k
            left = x
            
        return s