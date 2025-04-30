"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def path(node, curr):
            if not node:
                return curr
            
            curr.append(node)
            return path(node.parent, curr)
        
        p1 = path(p, [])
        p2 = path(q, [])
        
        if len(p1) < len(p2):
            seen = set(p1)
            for node in p2:
                if node in seen:
                    return node
        else:
            seen = set(p2)
            for node in p1:
                if node in seen:
                    return node