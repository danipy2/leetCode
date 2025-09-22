class Solution:
    def __init__(self):
        self.memo = [0]*46
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        if self.memo[n] == 0:
            self.memo[n] = self.climbStairs(n-1) +self.climbStairs(n-2)
        return self.memo[n]
            