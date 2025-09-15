class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        arr = text.split()
        s = set([i for i in brokenLetters])
        count  = 0
        for i in arr:
            for j in i:
                if j in s:
                    break
            else:
                count+=1
        return count
                
                
    