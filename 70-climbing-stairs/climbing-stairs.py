class Solution:
    def climbStairs(self, n: int) -> int:
        s = {}
        def f(r):
            if r in s:
                return s[r]
            v = 0
            if r-1>0:
                v += f(r-1)
            elif r-1 == 0:
                v += 1
            if r-2>0:
                v += f(r-2)
            elif r-2==0:
                v += 1
            s[r] = v
            return v
        f(n)
        return s[n]
            