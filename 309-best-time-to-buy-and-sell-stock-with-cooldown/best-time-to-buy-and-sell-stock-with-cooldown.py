class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [-1]*len(prices)

        def dp(s):
            if s>=len(memo):
                return 0
            if memo[s]==-1:
                maxm = 0
                for i in range(s+1,len(prices)):
                    if prices[s]<prices[i]:
                        diff = prices[i]-prices[s]
                        maxm = max(maxm,diff+dp(i+2))
                memo[s]  = max(maxm,dp(s+1))

            return memo[s]

        return dp(0)
            
            
