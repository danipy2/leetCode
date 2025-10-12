class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minm = prices[0]
        total = 0
        for i in prices:
            if i>minm:
                total += i-minm
                minm = i 
            minm = min(i,minm)
        return total