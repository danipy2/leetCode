class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        arr = [[0]*len(piles) for i in piles]
        def dp(l,r):
            if r<l:
                return 0
            if arr[l][r]==0:
                arr[l][r] = max(piles[l]+dp(l+1,r),dp(l,r-1)+piles[r])
            return arr[l][r]
        ans = dp(0,len(piles)-1) 
        return ans > sum(piles)-ans