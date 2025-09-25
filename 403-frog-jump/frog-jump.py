class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo= set()
        c = set(stones)
        def dp(stone,k):
            if k<=0:
                return False
            if stone == stones[-1]:
                return True
            if (stone,k) in memo:
                return False
            if stone not in c:
                return False
            memo.add((stone,k))
            if dp(stone+k+1,k+1) or dp(stone+k,k) or dp(stone+k-1,k-1):
                return True
            return False
        if stones[1] >1:
            return False
        return dp(stones[1],1)

