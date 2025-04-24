class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        elif n == 2:
            return 2
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

        # @lru_cache(maxsize=None)
        # def dp(remaining):
        #     if remaining == 0:
        #         # only when you reach the top is one way counted
        #         return 1
        #     elif remaining == 1:
        #         return 1
        #     elif remaining == 2:
        #         # either 1 step at a time or two steps at once
        #         return 2
            
        #     one = dp(remaining - 1)
        #     two = dp(remaining - 2)

        #     return one + two
        
        # return dp(n)