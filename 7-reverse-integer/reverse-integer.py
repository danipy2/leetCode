class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        y = abs(x)
        m = 2**31
        while y:
            a*=10
            a += y %10
            
            y = int(y/10)
            if (a==m and y>0) or a>m :
                return 0
        if x<0:
            a*=-1
        return a
        

        