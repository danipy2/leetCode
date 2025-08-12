class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        dirc = [(1,0),(0,1),(-1,0),(0,-1)]
        lans = 0
        def dfs(i,j):
            ans = 1
            for x,y in dirc:
                x += i
                y += j
                inbound = 0<=x<len(grid) and 0<=y<len(grid[0])
                if not inbound:
                    ans+= -25000
                if inbound and grid[x][y]:
                    grid[x][y] = 0
                    ans+= dfs(x,y)
            return ans
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    grid[i][j] = 0 
                    ans = dfs(i,j)
                    lans += max(0,ans)
        return lans

        