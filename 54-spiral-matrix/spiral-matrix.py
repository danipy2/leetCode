class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = left =  0 
        bottom = len(matrix)-1
        right = len(matrix[0])-1
        out = []
        while top <= bottom and left<=right:
            for i in range(left,right+1):
                out.append(matrix[top][i])
            top += 1
            print(out)
            for i in range(top,bottom+1):
                print(right,i)
                out.append(matrix[i][right])
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    out.append(matrix[bottom][i])
                bottom-=1
            if left <= right:
                for i in range(bottom,top-1,-1):
                    out.append(matrix[i][left])
                left += 1
        return out