class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        f = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    f += 1
        if f == 0:
            return 0
        t = 0
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        while q:
            s = len(q)
            for i in range(s):
                r, c = q.popleft()
                for dr, dc in dirs:
                    rr, cc = r + dr, c + dc
                    if rr < 0 or rr >= m:
                        continue
                    if cc < 0 or cc >= n:
                        continue

                    if grid[rr][cc] == 1:
                        grid[rr][cc] = 2
                        f -= 1
                        q.append((rr, cc))
            t += 1
        
        return t-1 if f == 0 else -1