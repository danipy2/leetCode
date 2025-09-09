class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        arr = [0]
        for i in range(len(s)):
            arr.append(arr[-1]+abs(ord(t[i])-ord(s[i])))
        l = 0
        maxm = 0
        for i in range(1,len(arr)):
            if arr[i]-arr[l] >maxCost:
                l+=1
            maxm = max(i-l,maxm)
        return maxm
                