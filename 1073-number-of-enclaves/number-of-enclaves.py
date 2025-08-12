class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        dirc = [(1,0),(0,1),(-1,0),(0,-1)]
        cond = True
        lans = 0
        def dfs(i,j):
            nonlocal cond
            ans = 1
            for x,y in dirc:
                x += i
                y += j
                inbound = 0<=x<len(grid) and 0<=y<len(grid[0])
                if not inbound:
                    cond = False
                    continue
                if grid[x][y]:
                    grid[x][y] = 0
                    ans+= dfs(x,y)
            return ans
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    cond = True
                    grid[i][j] = 0 
                    ans = dfs(i,j)
                    if cond:
                        lans += ans
        return lans

        