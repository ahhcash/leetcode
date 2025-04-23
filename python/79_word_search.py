class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        if not word:
            return True
        w = len(word)
        def dfs(i, j, idx):
            if idx == w:
                return True
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == '#':
                return False
            
            v = board[i][j]

            # prune the tree (but better)
            if not v == word[idx]:
                return False
            
            board[i][j] = '#'
            right = dfs(i, j+1, idx+1)
            down = dfs(i+1, j, idx+1)
            left = dfs(i, j-1, idx+1)
            up = dfs(i-1, j, idx+1)

            board[i][j] = v
            return right or down or left or up
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False
