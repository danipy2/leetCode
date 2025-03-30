class Solution:
    def pivotInteger(self, n: int) -> int:
        tot = 0
        tot2 = (n*(n+1))//2
        for i in range(1,n+1):
            if tot == tot2-tot-i:
                return i
            tot+=i
        return -1