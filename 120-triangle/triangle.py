class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo  = [[""]*len(triangle[i]) for i in range(len(triangle))]
        def dp(i,j):
            if i == len(triangle):
                return 0
            if memo[i][j] == "":
                memo[i][j] = min(dp(i+1,j),dp(i+1,j+1)) + triangle[i][j]
            return memo[i][j]
        return dp(0,0)

