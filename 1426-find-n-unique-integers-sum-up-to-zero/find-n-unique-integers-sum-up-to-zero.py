class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [i if i != n  else -(i*(i-1))//2 for i in range(1,n+1)] if n>1 else [0]