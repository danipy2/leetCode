class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m2 = prices[0]
        maxm = 0
        for i in prices:
            m2 = min(i,m2)
            maxm =max(maxm,i-m2) 
        return maxm