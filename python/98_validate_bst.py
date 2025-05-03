# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        res = []
        def inorder(node):
            nonlocal res
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        for i in range(1, len(res)):
            if res[i-1] >= res[i]:
                return False
        return True