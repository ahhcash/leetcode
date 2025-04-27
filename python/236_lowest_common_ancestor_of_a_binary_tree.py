# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node, p, q):
            if not node:
                return None
            
            leftpresent = lca(node.left, p, q)
            rightpresent = lca(node.right, p, q)

            if (leftpresent and rightpresent) or node in {p, q}: # this is the core condition that upper recursive calls will use
                return node
            else:
                return leftpresent if leftpresent else rightpresent
        
        return lca(root, p, q)