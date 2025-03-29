class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        t = 0
        arr = [-1,-1,-1]
        l = 0
        for i in range(len(s)):
            arr[ord(s[i])-ord('a')] = i
            t +=  min(arr[0],arr[1],arr[2])+1
        return t