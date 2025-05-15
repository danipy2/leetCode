class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        l = len(s)
        arr = []
        
        for i in range(1<<l):
            sub = []
            for j in range(l):
                if i & (1<<j):
                    if s[j].isalpha()==False:
                        break
                    sub.append(s[j].upper())
                else:
                    sub.append(s[j].lower())
            if len(sub)==l:
                arr.append("".join(sub))
        return arr