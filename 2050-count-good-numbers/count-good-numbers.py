class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def mult(x,p):
            total = 1
            mod = 1000000007
            while p:
                if p&1:
                    total  = (total *x) % mod
                x = (x*x)% mod
                p=p>>1
            return total
        return (mult(5,(n+1)//2) * mult(4,n//2)) % 1000000007
        
                