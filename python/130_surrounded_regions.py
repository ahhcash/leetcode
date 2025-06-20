class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        q = deque()
        m = len(board)
        n = len(board[0])
        edge = lambda r, c: r == 0 or r == m-1 or c == 0 or c == n-1
        for i in range(m):
            for j in range(n):
                if edge(i, j) and board[i][j] == 'O':
                    # to ohio in a swarm of bees
                    q.append((i, j))
                    board[i][j] = '#'
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                rr, cc = r + dr, c + dc
                if 0 <= rr < m and 0 <= cc < n and board[rr][cc] == 'O':
                    q.append((rr, cc))
                    board[rr][cc] = '#'
        
        for i in range(m):
            for j, c in enumerate(board[i]):
                board[i][j] = 'O' if c == '#' else 'X'