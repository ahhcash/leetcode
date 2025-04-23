# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = cur = ListNode()
        carry = 0
        prev = None
        while l1 and l2:
            v = carry + l1.val + l2.val
            carry, v = divmod(v, 10)
            cur.val = v
            cur.next = ListNode()
            prev = cur
            cur = cur.next

            l1 = l1.next
            l2 = l2.next
        
        while l1:
            v = carry + l1.val
            carry, v = divmod(v, 10)
            cur.val = v
            cur.next = ListNode()
            prev = cur

            cur = cur.next
            l1 = l1.next
        
        while l2:
            v = carry + l2.val
            carry, v = divmod(v, 10)
            cur.val = v
            cur.next = ListNode()
            prev = cur

            cur = cur.next
            l2 = l2.next
        
        if carry:
            cur.val = 1
        else:
            prev.next = None
        return head