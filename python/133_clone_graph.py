"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        if not node.neighbors: return Node(node.val)
        vis = {}
        def dfs(node):
            new = Node(node.val)
            vis[node] = new
            for nei in node.neighbors:
                if nei not in vis:
                    new.neighbors.append(dfs(nei))
                else:
                    new.neighbors.append(vis[nei])
            return new
        
        return dfs(node)
