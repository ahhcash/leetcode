# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -1001
        def mps(node):
            nonlocal ans
            if not node:
                return 0
            
            # max(0, ...) because we can choose to take this path or ignore entirely
            leftmax = max(0, mps(node.left))
            rightmax = max(0, mps(node.right))

            # now, within recurisve calls, if we find a good maximum that cuts the straight path, then this can be the final answer.
            # look at example test case 2
            ans = max(ans, node.val + leftmax + rightmax)

            return node.val + max(leftmax, rightmax)
        mps(root)
        return ans