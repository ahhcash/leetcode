# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-501, head)
        if left == right:
            return head
        
        prev, cur = dummy, head
        def reverse(bg, l, r):
            ag = r.next

            prev, cur = bg, l
            # print(f"in reverse, l: {l.val}, r: {r.val}, ag: {ag.val}, bg: {bg.val}")
            while not cur == ag:
                after = cur.next
                cur.next = prev
                prev = cur
                cur = after
            # print(f"after while. cur: {cur.val}")
            l.next = ag
            bg.next = r
        
        p = 1
        p1 = p2 = None
        prev1 = None
        while cur:
            # print(f"at {cur.val}")
            if p == left:
                p1 = cur
                prev1 = prev
            if p == right:
                p2 = cur
            prev = cur
            cur = cur.next
            p += 1
        # print(f"p1: {p1.val}, p2: {p2.val}")
        reverse(prev1, p1, p2)

        return dummy.next
        


