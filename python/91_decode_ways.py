class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0

        n = len(s)

        @lru_cache(None)
        def dp(i):
            if i == n: return 1
            if s[i] == "0": return 0
            
            ways = dp(i+1)
            if i+1 < n and int(s[i]+s[i+1]) <= 26:
                ways += dp(i+2)
            return ways
        
        return dp(0)