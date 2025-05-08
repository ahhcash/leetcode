# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(before_group, left, right):
            after_group = right.next

            prev, cur = before_group, left
            for _ in range(k):
                after = cur.next
                cur.next = prev
                prev = cur
                cur = after
            
            before_group.next = right
            left.next = after_group
            return left
        
        dummy = ListNode(-1, head)
        prev = dummy
        while True:
            c = 0
            r = prev
            for _ in range(k):
                r = r.next
                if not r:
                    break
                c += 1
            if c < k:
                break
            l = prev.next
            prev = reverse(prev, l, r)
        return dummy.next