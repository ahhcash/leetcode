class Solution:
    def totalNQueens(self, n: int) -> int:
        pos = set()
        neg = set()
        cols = set()
        ans = 0
        def dfs(row):
            nonlocal ans
            if row == n:
                ans += 1
                return
            
            for c in range(n):
                if c in cols or (row+c) in pos or (row-c) in neg: continue
                cols.add(c)
                pos.add(row+c)
                neg.add(row-c)

                dfs(row+1)

                cols.remove(c)
                pos.remove(row+c)
                neg.remove(row-c)
        dfs(0)
        return ans