class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = [max(grid[i]) for i in range(len(grid))]
        cols = []
        for i in range(len(grid[0])):
            maxm = 0
            for j in range(len(grid)):
                maxm = max(grid[j][i],maxm)
            cols.append(maxm)
        total = 0
        total1 = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total1 += grid[i][j]
                total += (min(rows[i],cols[j]))
        return total-total1
            
