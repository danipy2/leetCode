class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = []
        maxm = 0
       
        l = 0
        s = s.split()

        for i in s:
            maxm= max(maxm,len(i))
        while l < maxm:
            temp = []
            for i in s:
                val = i[l] if l<len(i) else " "
                temp.append(val)
            arr.append("".join(temp).rstrip())
            l+=1
        return arr

