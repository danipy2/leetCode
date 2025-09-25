class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount ==0:
            return 0
        lno = amount+1
        memo = [lno]*(amount+1)
        memo[0] = 0
        for coin in coins:
            for j in range(coin,amount+1):
                if memo[j- coin]!=lno:
                    memo[j] = min(memo[j],memo[j-coin]+1)
        return memo[amount] if memo[amount]!=lno else -1

        