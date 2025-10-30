class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        total = 1
        p = (n+1)//2
        x = 5
        mod = 1000000007
        while p:
            if p&1:
                total  = (total *x) % mod
            x = (x*x) %mod
            p=p>>1
        p = (n)//2
        x = 4
        while p:
            if p&1:
                total  = (total *x) % mod
            x = (x*x) % mod
            p=p>>1
        return total
        
                