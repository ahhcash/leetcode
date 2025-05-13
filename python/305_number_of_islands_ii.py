class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = [[0] * n for _ in range(m)]
        parent = {}
        def find(x):
            if not parent[x] == x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if not rootX == rootY:
                parent[rootY] = rootX
            
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        ans = [0] * len(positions)
        curri = 0
        for i, (r, c) in enumerate(positions):
            if grid[r][c] == 1:
                ans[i] = curri
            else:
                grid[r][c] = 1
                parent[(r, c)] = (r, c)
                curri += 1
                for dr, dc in dirs:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < m and 0 <= cc < n and grid[rr][cc] == 1:
                        if find((rr, cc)) != find((r, c)):
                            # they are neighboars and they belong to different sets, merge them and decrease island count by 1
                            curri -= 1
                            union((rr, cc), (r, c))
                ans[i] = curri

        return ans