class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        dp = [[0] * (m+1) for _ in range(n+1)]
        for k in range(m):
            dp[n][k] = m - k
        for k in range(n):
            dp[k][m] = n - k
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if not word1[i] == word2[j]:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1])
                else:
                    dp[i][j] = dp[i+1][j+1]
        
        return dp[0][0]

        # @lru_cache(maxsize=None)
        # def dp(i, j):
        #     if i == n:
        #         return m - j
            
        #     if j == m:
        #         return n - i
            
        #     if not word1[i] == word2[j]:
        #         return 1 + min(dp(i+1, j), dp(i, j+1))
        #     else:
        #         return dp(i+1, j+1)
        
        # return dp(0, 0)