# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwo(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            head = cur = ListNode()
            prev = None
            while l1 and l2:
                if l1.val < l2.val:
                    cur.val = l1.val
                    l1 = l1.next
                else:
                    cur.val = l2.val
                    l2 = l2.next
                cur.next = ListNode()
                prev = cur
                cur = cur.next
            
            if l1:
                prev.next = l1
            if l2:
                prev.next = l2
            
            return head
        
        def mergeK(listarr):
            if not listarr:
                return None
            elif len(listarr) == 1:
                return listarr[0]
            n = len(listarr)
            l1 = mergeK(listarr[:n//2])
            l2 = mergeK(listarr[n//2:])

            return mergeTwo(l1, l2)
        
        return mergeK(lists)
