class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        dirc = [(0,1),(1,0),(-1,0),(0,-1)]
        visted = set()
        self.cond = False
        self.c = False
        def dfs(x,y,p1,p2):
            visted.add((x,y))
            if self.cond:
                return 

            for i,j in dirc:
                nx = i+x
                ny = j+y
                
                isbound = 0<=nx<len(grid) and 0<=ny<len(grid[0])
                if isbound and grid[nx][ny] == grid[x][y]:
                    v = (nx,ny) in visted 
                    if v and (nx,ny) != (p1,p2):
                            self.cond = True 
                            return 
                    if not v:
                        dfs(nx,ny,x,y)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visted:
                    dfs(i,j,i,j)
        return self.cond
        
            

