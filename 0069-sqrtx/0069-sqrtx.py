class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while(left<=right):
            mid = (left + right) // 2
            if (mid*mid )<= x:
                if ((mid+1)*(mid+1)) > x:
                    return mid
                else:
                    left = mid+1
            else:
                right = mid -1
                
        return 0