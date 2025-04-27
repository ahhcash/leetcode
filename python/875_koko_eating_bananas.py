class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        def kokoEats(k, h):
            t = 0
            for pile in piles:
                t += ceil(pile/k)
            return t <= h
        l = 1
        r = max(piles)
        res = 1
        while l <= r:
            m = (l + r) // 2
            if kokoEats(m, h):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res
