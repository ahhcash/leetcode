class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = {i: i for i in range(1, n+1)}
        def find(x):
            if not parent[x] == x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if not rootX == rootY:
                parent[rootY] = rootX
        
        for u, v, _ in roads:
            if not find(u) == find(v):
                union(u, v)

        # guaranteed that 1 and n are in the same component, choose intermediate nodes such that they're in the same componnet
        ans = float('inf')
        for u, v, d in roads:
            if find(1) == find(u):
                ans = min(ans, d)
        
        return ans