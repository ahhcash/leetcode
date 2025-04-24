class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[0] * (amount + 1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        
        # have to go backwards because we would have computed dp[i+1][j] to re use
        for i in range(n-1, -1, -1):
            for j in range(1, amount+1):
                include = 0
                if coins[i] <= j:
                    include= dp[i][j-coins[i]]
                exclude = dp[i+1][j]
                dp[i][j]  = include + exclude

        return dp[0][amount]
        # @lru_cache(maxsize=None)
        # def dp(i, remaining):
        #     if i == n:
        #         return 0
        #     if remaining == 0:
        #         return 1
            
        #     if coins[i] <= remaining:
        #         # chhose the current one, BUT also try skipping and finding combinations that could exist without this coin
        #         return dp(i, remaining - coins[i]) + dp(i+1, remaining)
        #     else:
        #         # the current coin is too big, skip and try a different one
        #         return dp(i+1, remaining)
        # return dp(0, amount)