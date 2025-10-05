class Solution:
    def numSquares(self, n: int) -> int:
        val = []
        for i in range(1,n+1):
            v = math.sqrt(i) 
            if v == int(v):
                val.append(i)
        bu = [[0]*(n+1) for i in range(len(val))]
        for i in range(1,n+1):
            bu[0][i] = bu[0][i-val[0]]+1
        for i in range(1,len(val)):
            for j in range(1,n+1):
                bu[i][j] = min(bu[i][j-val[i]]+1,bu[i-1][j]) if j>= val[i] else bu[i-1][j]
        return bu[-1][-1]

        