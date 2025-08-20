class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        s1 = set()
        s2 = set()
        s3 = set()
        def dfs(row,placed):
            nonlocal count
            if row==n:
                if placed ==n:
                    count +=1
                return 
            
            for col in range(n):
                if row+col not in s3 and row-col not in s2 and col not in s1:
                    s1.add(col)
                    s2.add(row-col)
                    s3.add(row+col)
                    dfs(row+1,placed+1)
                    s1.remove(col)
                    s2.remove(row-col)
                    s3.remove(row+col)
        row = 0
        dfs(0,0)
        return count