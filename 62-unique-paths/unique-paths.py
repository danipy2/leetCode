class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def fact(x):
            total = 1
            while x>1:
                total*= x
                x-=1
            return total
        total = fact(m+n-2)//(fact(m-1)* fact(n-1))
        return total