class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        inf = float('inf')
        dist = [[inf] * m for _ in range(n)]
        dist[0][0] = 0
        pq = []
        heappush(pq, (0, 0, 0))
        vis = set()
        vis.add((0, 0))
        while pq:
            d, r, c = heappop(pq)
            for dr, dc in dirs:
                rr, cc = r + dr, c + dc
                if 0 <= rr < n and 0 <= cc < m and (rr, cc) not in vis:
                    diff = max(d, moveTime[rr][cc]) + 1
                    if diff < dist[rr][cc]:
                        dist[rr][cc] = diff
                        heappush(pq, (diff, rr, cc))
                    vis.add((rr, cc))
        
        return dist[n-1][m-1]