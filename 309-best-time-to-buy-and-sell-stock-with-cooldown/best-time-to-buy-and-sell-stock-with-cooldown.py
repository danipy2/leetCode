class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        table = [0]*len(prices)
        for i in range(len(prices)-1,-1,-1):
            maxm = table[i+1] if i != len(prices)-1 else 0 
            for j in range(len(prices)-1,i,-1):
                maxm = max(maxm,prices[j]-prices[i]+(table[j+2] if j+2<len(table) else 0))
            table[i] = maxm
        return table[0]
            
            
            
