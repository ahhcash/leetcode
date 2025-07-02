class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        m, n = len(w1), len(w2)

        @lru_cache(None)
        def dp(i, j):
            if i == m:
                return n-j
            if j == n:
                return m-i
            
            if w1[i] == w2[j]:
                return dp(i+1, j+1)
            else:
                return 1 + min(dp(i+1, j+1), dp(i+1, j), dp(i, j+1))
        
        return dp(0, 0)