class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1 ,l2 = 0,len(matrix[0])-1
        r1 ,r2 = len(matrix)-1,0
        while l1<len(matrix) and matrix[l1][l2] < target:
            l1+=1
        while r1>0 and matrix[r1][0] > target:
            r1-=1
        for i in range(l1,r1+1):
            ind = bisect_left(matrix[i],target)
            if ind<= l2 and matrix[i][ind] == target:
                return True
        return False
        

