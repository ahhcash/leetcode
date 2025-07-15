class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        r, c = startPos
        targetr, targetc = homePos
        ans = 0
        ro = -1 if targetr < r else 1
        while not r == targetr:
            r += ro
            ans += rowCosts[r]
        
        co = -1 if targetc < c else 1
        while not c == targetc:
            c += co
            ans += colCosts[c]
        return ans

