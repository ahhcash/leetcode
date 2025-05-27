# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        tortoise = head
        hare = head

        while True:
            tortoise = tortoise.next
            hare = hare.next.next if hare.next else None
        
            if not tortoise or not hare: return None
            if tortoise == hare: break
        
        # print(f"meeting point: {tortoise.val} == {hare.val}")
        cur = head
        while True:
            if cur == tortoise:
                break
            
            cur = cur.next
            tortoise = tortoise.next
            
        return cur