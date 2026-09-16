# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        first = True

        while fast is not None and fast.next is not None:
            if slow == fast and not first:
                return True
            first = False

            slow = slow.next
            fast = fast.next.next
        
        return False

    