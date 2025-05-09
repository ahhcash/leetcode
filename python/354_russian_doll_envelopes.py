class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n == 0:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        @lru_cache(maxsize=None)
        def dp(i, prevh):
            if i == n:
                return 0
            
            wi, hi = envelopes[i]
            skip = dp(i+1, prevh)
            take = 0
            if hi > prevh:
                take = 1 + dp(i+1, hi)
            
            return max(take, skip)

        res = dp(0, 0)
        return res
    
