class Solution:
    def numRescueBoats(self, wts: List[int], limit: int) -> int:
        wts.sort()
        n = len(wts)
        c = 0
        res = 0
        l, r = 0, n-1
        while l < r:
            if wts[l] + wts[r] <= limit:
                l += 1
                r -= 1
                c += 2
            else:
                r -= 1
                c += 1
            res += 1
        if c < n and wts[l] <= limit:
            res += 1
        return res