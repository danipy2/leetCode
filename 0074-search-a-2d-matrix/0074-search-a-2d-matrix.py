class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) *len(matrix[0])-1
        while(left<=right):
            mid = (left+right)//2
            fdim = mid//(len(matrix[0]))
            sdim = mid % (len(matrix[0]))
            if matrix[fdim][sdim] == target:
                return True
            elif  matrix[fdim][sdim] < target:
                left = mid +1
            else:
                right = mid -1
        return False