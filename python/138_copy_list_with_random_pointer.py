"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        memo = {}
        cur = head
        while cur:
            node = Node(cur.val)
            memo[cur] = node
            cur = cur.next
        
        cur = head
        while cur:
            memo[cur].next = memo[cur.next] if cur.next else None
            memo[cur].random = memo[cur.random] if cur.random else None
            cur = cur.next
        
        return memo[head]