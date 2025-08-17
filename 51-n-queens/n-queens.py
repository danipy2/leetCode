class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def inbound(x,y):
            return 0<= x < n and 0<= y < n
        set1 = {}
        set2 = {}
        set3 = {}
        set5 = {}

        def markattack(x,y,c):
            set1[x] = set1.get(x,0) + c
            set2[x+y] = set2.get(x+y,0) + c
            set3[x-y] = set3.get(x-y,0) + c
            set5[y] = set5.get(y,0)+c
        set4 = set()
        def putans():
                b = [["."] * n for i in range(n)]
                for (i,j) in set4:
                    b[i][j]="Q"
                ans.append(["".join(b[i]) for i in range(n)])
        def putqueen(x,y,c):
            set4.add((x,y))
            if c==1:
                putans()
                set4.remove((x,y))
                return
            markattack(x,y,1)
            x1 = x+1
            y1 = 0
            for i in range(x1,n):
                for j in range(y1,n):
                    if not set1.get(i,0) and not set2.get(i+j,0) and not set3.get(i-j,0) and not set5.get(j,0):
                        putqueen(i,j,c-1)
                        
            markattack(x,y,-1)
            set4.remove((x,y))
        for i in range(n):
            for j in range(n):
                putqueen(i,j,n)
        return ans

            

