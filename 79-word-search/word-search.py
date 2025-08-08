class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.cond = False
        self.word = word
        visted = set()
        dirc = [(0,1),(1,0),(-1,0),(0,-1)]
        def inbound(x,y):
            return 0<=x<len(board) and 0<=y<len(board[0])
        def dfs(x,y,t):
            visted.add((x,y))
            if len(visted)== len(self.word) or self.cond:
                self.cond = True
                return 
            for i,j in dirc:
                nx = x+i
                ny = y+j
                if inbound(nx,ny) and (nx,ny) not in visted and  board[nx][ny] == self.word[t]:
                    dfs(nx,ny,t+1)
            visted.remove((x,y))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    dfs(i,j,1)
                    visted = set()
                if self.cond:
                    break
            if self.cond:
                break
        return self.cond