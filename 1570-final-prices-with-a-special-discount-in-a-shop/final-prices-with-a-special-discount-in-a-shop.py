class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for key ,value in enumerate(prices):
            while stack and prices[stack[-1]] >= value:
                prices[stack.pop()] -= value
            stack.append(key)
        return prices
