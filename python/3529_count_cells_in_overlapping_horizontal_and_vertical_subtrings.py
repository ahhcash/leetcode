class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        horizontal = ""
        vertical = ""

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                horizontal += grid[i][j]
        
        for j in range(cols):
            for i in range(rows):
                vertical += grid[i][j]
        
        # print(f"horizontal: {horizontal}, vertical: {vertical}")
        horizontalhits = []
        verticalhits = []
        pos = horizontal.find(pattern, 0)
        while pos >= 0:
            horizontalhits.append((pos, pos+len(pattern)))
            pos = horizontal.find(pattern, pos+1)
        
        pos = vertical.find(pattern, 0)
        while pos >= 0:
            verticalhits.append((pos, pos+len(pattern)))
            pos = vertical.find(pattern, pos+1)
        
        hprefix = [0] * len(horizontal)
        vprefix = [0] * len(vertical)

        for s, e in horizontalhits:
            if s < len(horizontal): hprefix[s] += 1
            if e < len(horizontal): hprefix[e] -= 1
        
        for s, e in verticalhits:
            if s < len(vertical): vprefix[s] += 1
            if e < len(vertical): vprefix[e] -= 1
        
        for i in range(1, len(hprefix)):
            hprefix[i] += hprefix[i-1]
        
        for i in range(1, len(vprefix)):
            vprefix[i] += vprefix[i-1]
        
        # print(f"hprefix: {hprefix}\nvpreifx: {vprefix}")
        g1 = [[0] * cols for _ in range(rows)]
        g2 = [[0] * cols for _ in range(rows)]

        for i in range(len(hprefix)):
            r, c = divmod(i, cols)
            g1[r][c] = hprefix[i]
        
        for i in range(len(vprefix)):
            c, r = divmod(i, rows)
            g2[r][c] = vprefix[i]
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if g1[i][j] > 0 and g2[i][j] > 0:
                    ans += 1

        return ans