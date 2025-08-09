class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        dirc = [(0,1),(1,0),(-1,0),(0,-1)]
        self.cond = False
        def dfs(x,y,p1,p2):
            letter = grid[x][y]
            if self.cond:
                return 
            grid[x][y] = ""
            
            for i,j in dirc:
                nx = i+x
                ny = j+y
                
                isbound = 0<=nx<len(grid) and 0<=ny<len(grid[0])
                if isbound:
                    if grid[nx][ny] == letter:
                        dfs(nx,ny,x,y)
                    elif grid[nx][ny] ==""  and (nx,ny)!= (p1,p2):
                        self.cond = True 
                        break  
            grid[x][y] = "*"
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != "*":
                    dfs(i,j,i,j)
                    if self.cond:
                        return True
        return self.cond
        
            

