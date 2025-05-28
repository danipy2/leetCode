class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirc = [(1,0),(-1,0),(0,1),(0,-1)]
        def inbound(x,y):
            return 0<=x<len(board) and 0<=y<len(board[0])
        visted = set()
        def dfs(x,y):
            if (x,y) in visted:
                return True
            visted.add((x,y))
            for l,r in dirc:
                cx = x+l
                cy = y+r
                if  inbound(cx,cy) and board[cx][cy] == "O" :
                    dfs(cx,cy)
        row = len(board)
        col  = len(board[0])
        for i in range(len(board)):
            if (i,0) not in visted and board[i][0] =="O":
                    dfs(i,0)
        for j in range(len(board[0])):
                if (0,j) not in visted and board[0][j] =="O":
                    dfs(0,j)
        for j in range(1,col):

                print(row-1,j)
                if (row-1,j) not in visted and board[row-1][j] =="O":
                    dfs(row-1,j)
        for j in range(1,row):
                if (j,col-1) not in visted and board[j][col-1] =="O":
                    dfs(j,col-1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in visted:
                    board[i][j] ="X"