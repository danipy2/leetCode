class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        memo= set()
        c = {}
        for i in range(len(stones)):
            stone = stones[i]
            c[stone] = i
        def dp(i,k):
            if k<=0:
                return False
            if i+1 >= len(stones):
                return True
            if (i,k) in memo:
                return False
            memo.add((i,k))
            curr = stones[i]
            n1 = curr+k+1
            n2 = curr+k
            n3 = curr+k-1
            if n1 in c:
                if dp(c[n1],k+1):
                    return True
            if n2 in c:
                if dp(c[n2],k):
                    return True
            if n3 in c and dp(c[n3],k-1):
                    return True
            return False
        if stones[1] >1:
            return False
        return dp(1,1)

