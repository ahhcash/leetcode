class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = {
        (1, 3): 2, (3, 1): 2,
        (1, 7): 4, (7, 1): 4,
        (1, 9): 5, (9, 1): 5,
        (2, 8): 5, (8, 2): 5,
        (3, 7): 5, (7, 3): 5,
        (3, 9): 6, (9, 3): 6,
        (4, 6): 5, (6, 4): 5,
        (7, 9): 8, (9, 7): 8
        }
        
        ans = 0
        vis = set()
        def dfs(k, c):
            nonlocal ans
            if c >= m:
                ans += 1
            if c >= n:
                return
            for i in range(1, 10):
                if i == k or i in vis: continue
                jumped = skip.get((k, i))
                if not jumped or jumped in vis:
                    vis.add(i)
                    dfs(i, c+1)
                    vis.discard(i)
        
        for i in range(1, 10):
            vis.add(i)
            dfs(i, 1)
            vis.discard(i)
        
        return ans