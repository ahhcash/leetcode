class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        pq = []
        m, n = len(grid), len(grid[0])
        scores = [[-1] * n for _ in range(m)]

        pq.append((-grid[0][0], 0, 0))
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        while pq:
            score, r, c, = heappop(pq)
            score = -score
            
            if r == m-1 and c == n-1:
                return score
            
            for dr, dc in dirs:
                rr, cc = r + dr, c + dc
                if 0 <= rr < m and 0 <= cc < n:
                    minscore = min(score, grid[rr][cc])
                    if scores[rr][cc] < minscore:
                        scores[rr][cc] = minscore
                        heappush(pq, (-minscore, rr, cc))
        
        return scores[m-1][n-1]