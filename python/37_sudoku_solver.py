class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        sub = [set() for _ in range(9)]
        empty = []
        for i in range(9):
            for j in range(9):
                if not board[i][j] == ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    sub[(i//3)*3+j//3].add(board[i][j])
                else:
                    empty.append((i, j))

        def dfs(e):
            if e == len(empty):
                return True
            i, j = empty[e][0], empty[e][1]
            for n in "123456789":
                s = (i//3)*3 + j//3
                seen = (
                    n in rows[i] or
                    n in cols[j] or
                    n in sub[s]
                )
                if seen: continue
                board[i][j] = n
                rows[i].add(n)
                cols[j].add(n)
                sub[s].add(n)
                if dfs(e+1):
                    return True
                board[i][j] = "."
                rows[i].discard(n)
                cols[j].discard(n)
                sub[s].discard(n)
            return False
                    
        dfs(0)