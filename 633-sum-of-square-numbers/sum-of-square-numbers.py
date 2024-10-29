class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = 0
        myd = {}
        arr = []
        if c<=1:
            return True
        while(n*n) <= c:
            myd[n*n] = n
            arr.append(n*n)
            
            n+=1
        left = 0
        right = len(arr)-1
        while(left<=right):
            if arr[left] +arr[right]==c:
                return True
            elif arr[left] +arr[right] > c:
                right-=1
            else:
                left+=1
        return False

        return False
        

        