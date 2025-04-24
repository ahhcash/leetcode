class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            minval = float('inf')
            for coin in coins:
                if coin <= i:
                    minval = min(minval, 1 + dp[i-coin])
            dp[i] = minval

        return dp[amount] if not dp[amount] == float('inf') else -1


        # @lru_cache(maxsize=None)
        # def dp(remaining):
        #     if remaining == 0:
        #         return 0
            
        #     minval = float('inf')
        #     for coin in coins:
        #         if coin <= remaining:
        #             minval = min(minval, 1 + dp(remaining - coin))
        #     return minval

        # res = dp(amount)

        # return -1 if res == float('inf') else res