# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow dhould be the middle
        l1 = head
        l2 = slow.next
        
        # only one element
        if not l2:
            return head
        
        # disconnect the lists
        slow.next = None
        
        prev, after = None, l2.next
        # reverse second half using same logic as reverse linked list
        while after:
            l2.next = prev
            prev = l2
            l2 = after
            after = after.next
        l2.next = prev

        while l2:
            t1 = l1.next
            t2 = l2.next

            l1.next = l2
            l2.next = t1

            l1 = t1
            l2 = t2
        return head
