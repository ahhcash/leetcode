class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        l = min(x for x, _, _ in squares)
        r = max(y+s for _, y, s in squares)
        n = len(squares)

        tolerance = 1e-5
        while r - l > tolerance:
            m = (l + r) / 2
            below = above = 0
            for i in range(n):
                x, y, s = squares[i]
                yy = y + s
                if yy <= m:
                    below += s * s
                elif y >= m:
                    above += s * s
                else:
                    below += (m - y) * s
                    above += (yy - m) * s
            
            if above > below:
                l = m
            else:
                r = m
        return l
