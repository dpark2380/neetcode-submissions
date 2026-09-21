# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return None

        length = 0
        cur = head
        while cur is not None:
            length += 1
            cur = cur.next
        
        cur = head
        prev = None
        req = length - n
        while req != 0:
            prev = cur
            cur = cur.next
            req -= 1
        
        if prev == None:
            return cur.next

        after = cur.next
        prev.next = after

        return head
