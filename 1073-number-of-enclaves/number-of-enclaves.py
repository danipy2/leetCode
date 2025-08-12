class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        dirc = [(1,0),(0,1),(-1,0),(0,-1)]
        lans = 0
        w,h = len(grid),len(grid[0])
        def dfs(i,j):
            for x,y in dirc:
                x += i
                y += j
                inbound = 0<=x<len(grid) and 0<=y<len(grid[0])
                if inbound and grid[x][y]:
                    grid[x][y] = 0
                    dfs(x,y)
        for i in range(0,w,max(1,w-1)):
            for j in range(h):
                if grid[i][j]:
                    grid[i][j] = 0
                    dfs(i,j)
        for i in range(0,h,max(h-1,1)):
            for j in range(w):
                if grid[j][i]:
                    grid[j][i] = 0
                    dfs(j,i)
        count = 0
        for i in range(len(grid)):
            for j in grid[i]:
                count+= j
        return count
        

        