class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        while(left<=right):
            i = (left+right)//2
            if matrix[i][0] == target:
                return True
            elif matrix[i][0] < target:
                left+=1
            else:
                right-=1
        l = 0
        r = len(matrix[left-1])-1
        while(l<=r):
            i = (l+r)//2
            if matrix[left-1][i] == target:
                return True
            elif matrix[left-1][i] < target:
                l+=1
            else:
                r-=1
        return False


