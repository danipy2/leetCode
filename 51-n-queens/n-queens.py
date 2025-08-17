class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0] * n for i in range(n)]
        ans = []
        def inbound(x,y):
            return 0<= x < n and 0<= y < n
        def markattack(x,y,s):
            yl = y-1
            while 0<= yl < n:
                board[x][yl] += s
                yl-= 1
            yr = y+1
            while 0<= yr < n:
                board[x][yr] += s
                yr+= 1
            xl = x-1
            while 0<= xl <  n:
                board[xl][y] += s
                xl-=1 
            xr = x+1
            while 0<= xr < n:
                board[xr][y] += s
                xr+= 1
            xl,yl = x-1,y-1
            while inbound(xl,yl):
                board[xl][yl] += s
                yl-=1
                xl-=1
            xr,yr = x+1,y+1
            while inbound(xr,yr):
                board[xr][yr] += s
                yr+=1
                xr+=1
            xl,yr = x-1,y+1
            while inbound(xl,yr):
                board[xl][yr] += s
                yr+=1
                xl-=1
            xr,yl = x+1,y-1
            while inbound(xr,yl):
                board[xr][yl] += s
                yl-=1
                xr+=1
        def putans():
                b = [[0] * n for i in range(n)]
                for x in range(n):
                    for y in range(n):
                        if board[x][y]==0:
                            b[x][y]="Q"
                        else:
                            b[x][y]="."
                ans.append(["".join(b[i]) for i in range(n)])
        def putqueen(x,y,c):
            markattack(x,y,1)
            if c==1:
                putans()
                pass
            x1 = x+1
            y1 = 0
            for i in range(x1,n):
                for j in range(y1,n):
                    if board[i][j]==0:
                        putqueen(i,j,c-1)
            markattack(x,y,-1)
        for i in range(n):
            for j in range(n):
                if putqueen(i,j,n) :
                    board = [[0] * n for i in range(n)]
        return ans

            

