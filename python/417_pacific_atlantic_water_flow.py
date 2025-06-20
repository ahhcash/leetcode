class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        def bfs(start):
            vis = set(start)
            q = deque(start)

            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < m and 0 <= cc < n and heights[rr][cc] >= heights[r][c] and (rr, cc) not in vis:
                        vis.add((rr, cc))
                        q.append((rr, cc))
            
            return vis
        # simply find the common visited cells
        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(m)]
        atlantic = [(m-1, i) for i in range(n)] + [(i, n-1) for i in range(m)]

        pvis = bfs(pacific)
        avis = bfs(atlantic)

        return [[r, c] for r, c in pvis & avis]