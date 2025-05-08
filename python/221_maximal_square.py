class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = -float('inf')

        dpp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    dpp[i][j] = 1 + min(dpp[i][j+1], dpp[i+1][j], dpp[i+1][j+1])
        for i in range(len(dpp)):
            ans = max(ans, max(dpp[i]))
        
        return ans * ans
        # @lru_cache(maxsize=None)
        # def dp(i, j):
        #     nonlocal ans
        #     if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] == '0':
        #         return 0

        #     if matrix[i][j] == '1':
        #         return 1 + min(dp(i, j+1), dp(i+1, j), dp(i+1, j+1))
        
        # for x in range(m):
        #     for y in range(n):
        #         val = dp(x, y)
        #         ans = max(ans, val)
                
        # return ans * ans