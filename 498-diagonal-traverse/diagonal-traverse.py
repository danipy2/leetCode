class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = 0
        col = 0
        d = 1 
        output = []
        while row <len(mat) and  col<len(mat[0]):
            output.append(mat[row][col])
            if d ==1:
                if col == len(mat[0])-1:
                    row+=1
                    d-=1
                elif row == 0:
                    col+=1
                    d-=1
                else:
                    row-=1
                    col+=1
            else:
                if row == len(mat)-1:
                    col+=1
                    d+=1
                elif col == 0:
                    row+=1
                    d+=1
                else:
                    row+=1
                    col-=1
        return output

