class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqr = 0
        myset = set()
        n = 0
        while n <= c:
            sqr = n*n
            myset.add(sqr)
            if sqr >c:
                return False
            if c-sqr in myset:
                return True
            n+=1