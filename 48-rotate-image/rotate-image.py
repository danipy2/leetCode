class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = 0
        j = 0
        while(i<len(matrix) and j<len(matrix)):
            k = i
            l = j
            while k>l:
                matrix[k][l],matrix[l][k] = matrix[l][k],matrix[k][l]
                k-=1
                l+=1
            if i < (len(matrix)-1):
                i+=1
            else:
                j+=1
            

                

        for i in range(len(matrix)):
            l = 0
            r = len(matrix[i])-1
            while l<r:
                matrix[i][l],matrix[i][r]=matrix[i][r],matrix[i][l]
                l+=1
                r-=1
        