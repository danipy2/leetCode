class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix2 = [[0]*len(matrix) for _ in range(len(matrix[0]))]
        
        for i in range(len(matrix[0])):

            for j in range(len(matrix)):
                 matrix2[i][j]=(matrix[j][i])
           
                
        return matrix2
                
            
            

        