class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target:
            return True
        n = m = len(mat)
        for k in range(4):
            newarr = [[mat[j][i] for j in range(m)]for i in range(n-1,-1,-1)]
            if newarr == target:
                return True
            mat = [newarr[i].copy() for i in range(n)]
        return False
