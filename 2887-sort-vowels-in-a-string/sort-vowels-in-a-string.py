class Solution:
    def sortVowels(self, s: str) -> str:
        vow = {"A":0,"E":0,"I":0,"O":0,"U":0,"a":0,"e":0,"i":0,"o":0,"u":0}
        for i in s:
            if i in vow:
                vow[i]+=1
        l = 0
        arr = list(s)
        for i in vow:
            while vow[i]:
                if arr[l] in vow:
                    vow[i]-=1
                    arr[l] = i 
                l+=1
        return "".join(arr)