# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}        

        def dp(node):
            if not node:
                return 0
            if node in memo:
                return memo[node]

            take = node.val
            if node.left:
                take += (dp(node.left.left) + dp(node.left.right))
            if node.right:
                take += (dp(node.right.left) + dp(node.right.right))
            
            skip = dp(node.left) + dp(node.right)

            memo[node] = max(take, skip)

            return memo[node]
        
        return dp(root)