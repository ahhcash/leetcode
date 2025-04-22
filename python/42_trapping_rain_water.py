class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        lefts = [0] * n
        rights = [0] * n
        
        maxl = height[0]
        for i in range(n):
            lefts[i] = maxl
            maxl = max(maxl, height[i])

        maxr = height[-1]
        for i in range(n-1, -1, -1):
            rights[i] = maxr
            maxr = max(maxr, height[i])
        
        for i in range(n):
            l = lefts[i]
            r = rights[i]
            res += max(0, min(l, r) - height[i])
        
        return res
        
