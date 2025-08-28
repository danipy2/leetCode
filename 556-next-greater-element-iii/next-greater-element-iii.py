class Solution:
    def nextGreaterElement(self, n: int) -> int:
        word = [int(i) for i in str(n)]
        p = 0
        for i in range(len(word)-2,-1,-1):
            if word[i] < word[i+1]:
                c = word[i]
                
                l=len(word)-1
                p=l
                while l>i and word[l]<=c:
                    p = l-1
                    l-=1
                word[i],word[p] = word[p],word[i]
                p=i+1
                break
        else:
            return -1

        word = word[:p]+sorted(word[p:])
        m = int("".join([str(i) for i in word]))

        return m if m < (2**31  )else -1
