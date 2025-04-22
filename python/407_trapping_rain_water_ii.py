class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        pq = []
        vis = [[False] * n for _ in range(m)]
        # start from the boundary and beign to find 'basins' - areas that can collect water
        for k in range(n):
            heappush(pq, (heightMap[0][k], 0, k))
            heappush(pq, (heightMap[m-1][k], m-1, k))
            vis[0][k] = True
            vis[m-1][k] = True

        for k in range(m):
            heappush(pq, (heightMap[k][0], k, 0))
            heappush(pq, (heightMap[k][n-1], k, n-1))
            vis[k][0] = True
            vis[k][n-1] = True

        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        res = 0
        while pq:
            h, r, c = heappop(pq)
            for dr, dc in dirs:
                rr, cc = r + dr, c + dc
                if rr < 0 or rr >= m:
                    continue
                if cc < 0 or cc >= n:
                    continue

                if not vis[rr][cc]:
                    vis[rr][cc] = True
                    # we're currently at a boundary (r, c) and a neighbor is smaller (rr, cc). this means it can trap water!
                    if heightMap[rr][cc] < h:
                        res += (h - heightMap[rr][cc])
                        # cells inside would also be bounded by the current wall (r, c woth height h)
                        heappush(pq, (h, rr, cc))
                    else:
                        # a neighbor is taller, this becomes the new boundary
                        heappush(pq, (heightMap[rr][cc], rr, cc))
        
        return res

