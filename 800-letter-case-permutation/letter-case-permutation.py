class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        l = 0
        ind = []
        for i in range(len(s)):
            if s[i].isalpha():
                ind.append(i)
                l+=1
        arr =[]
        su = list(s)
        for i in range(1<<l):
            sub = su
            for j in range(l):
                    if i & (1<<j):
                        sub[ind[j]] = sub[ind[j]].upper()
                    else:
                        sub[ind[j]] = sub[ind[j]].lower()
            arr.append("".join(sub))
        return arr