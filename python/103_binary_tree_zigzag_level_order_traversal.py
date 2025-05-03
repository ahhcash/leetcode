# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        res = []
        q.append(root)
        i = 0
        while q:
            s = len(q)
            t = []
            for _ in range(s):
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                t.append(q.popleft().val)
            if i % 2 == 0:
                res.append(t)
            else:
                res.append(t[::-1])
            i += 1
        
        return res