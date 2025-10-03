class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        table = [[0,0,0] for i in range(n)]
        table[0][0] = -prices[0]
        for i in range(1,n):
            table[i][0] = max(table[i-1][0],table[i-1][1]-prices[i]) 
            table[i][1] = max(table[i-1][1],table[i-1][2])
            table[i][2] = table[i-1][0] + prices[i]
        return max(table[-1][1],table[-1][2])
            
            
            
