# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        cur = prev = dummy
        while cur:
            cur = cur.next
            if n < 0:
                prev = prev.next
            else:
                n -= 1
        
        if prev.next:
            prev.next = prev.next.next
        else:
            prev.next = None
        return dummy.next