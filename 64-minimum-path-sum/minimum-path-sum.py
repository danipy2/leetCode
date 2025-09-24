class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = [[-1]*len(grid[0]) for i in range(len(grid))]
        def dp(i,j):
            m,n = len(grid),len(grid[0])
            if i==m or j==n :
                return float("inf")
            if i==m-1 and j==n-1:
                return grid[i][j]
            if memo[i][j]==-1:
                memo[i][j] = min(dp(i+1,j), dp(i,j+1)) + grid[i][j]
            return memo[i][j]
        
        return dp(0,0)