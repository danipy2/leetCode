class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i>0:
                    mat[i][j] += mat[i-1][j]
                if j>0:
                    mat[i][j] += mat[i][j-1]
                if i>0 and j>0:
                    mat[i][j] -= mat[i-1][j-1]
        out = []
        for i in range(len(mat)):
            arr = []
            for j in range(len(mat[i])):
                total = 0
                right_row = i+k
                right_col = j+k
                left_row = i-k
                left_col = j-k
                if right_row>=len(mat):
                    right_row = len(mat)-1
                if right_col >= len(mat[i]):
                    right_col = len(mat[i])-1
                
                total+= mat[right_row][right_col]
                if left_row >0:
                    total -= mat[left_row-1][right_col]
                if left_col > 0:
                    total -= mat[right_row][left_col-1]
                if left_row>0 and left_col>0:
                    total += mat[left_row-1][left_col-1]
                arr.append(total)
            out.append(arr)
        return out
