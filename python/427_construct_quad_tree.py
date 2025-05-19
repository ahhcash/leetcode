"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        def same(x, y, l):
            val = grid[x][y]
            for i in range(l):
                for j in range(l):
                    if not val == grid[x+i][y+j]:
                        return False

            return True
        
        def build(x, y, sz):
            # print(f"build with size: {sz}")
            if sz == 1:
                val = int(grid[x][y] == 1)
                isLeaf = True
                return Node(val, isLeaf, None, None, None, None)
            else:
                if same(x, y, sz):
                    val = int(grid[x][y] == 1)
                    return Node(val, True, None, None, None)
                else:
                    half = sz // 2
                    tl = build(x, y, half)
                    bl = build(x + half, y, half)
                    tr = build(x, y + half, half)
                    br = build(x + half, y + half, half)
                    isLeaf = False
                    return Node(1, isLeaf, tl, tr, bl, br)
        
        return build(0, 0, n)