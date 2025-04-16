class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_grid(i, j):
            seen = set()
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    if not board[x][y] == ".":
                        if board[x][y] in seen:
                            return False
                        seen.add(board[x][y])
            return True
        
        for x in range(9):
            rseen = set()
            cseen = set()
            for y in range(9):
                if not board[x][y] == ".":
                    if board[x][y] in rseen:
                        return False
                    rseen.add(board[x][y])

                if not board[y][x] == ".":
                    if board[y][x] in cseen:
                        return False
                    cseen.add(board[y][x])
        
        # check each grid
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                if not check_grid(x, y):
                    return False
        
        return True
