class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        s = 2 ** n
        grid = [[0] * s for _ in range(s)]
        def fill(i, j, sz, val):
            if sz == 1:
                grid[i][j] = val
            elif sz == 2:
                grid[i][j] = val
                grid[i+1][j] = val-1
                grid[i+1][j+1] = val-2
                grid[i][j+1] = val-3
            else:
                dec = (sz//2) ** 2
                fill(i, j, sz//2, val)
                fill(i+sz//2, j, sz//2, val-dec)
                fill(i+sz//2, j+sz//2, sz//2, val-2*dec)
                fill(i, j+sz//2, sz//2, val-3*dec)
        
        fill(0, 0, s, 2**(2*n) - 1)
        return grid