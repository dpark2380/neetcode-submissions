# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        stack = []
        cur = head
        length = 0
        while cur is not None:
            length += 1
            cur = cur.next

        cur = head
        mid = (length + 1) // 2
        while mid != 0:
            cur = cur.next
            mid -= 1
        
        while cur is not None:
            stack.append(cur)
            cur = cur.next

        cur = head
        mid = (length + 1) // 2
        while stack:
            after = cur.next
            val = stack.pop()

            cur.next = val
            val.next = after

            cur = after
                
        if cur:
            cur.next = None





