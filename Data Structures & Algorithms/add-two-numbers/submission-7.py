# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2

        # initialising starting node.
        start = ListNode()
        prev = start

        # Variable to track whether or not we have a carry on.
        carry = 0

        # Looping while at least one of the pointer is not null or carry is 1.
        while cur1 or cur2 or carry:
            v1 = cur1.val if cur1 else 0
            v2 = cur2.val if cur2 else 0
            
            val = v1 + v2 + carry
            digit = val % 10
            carry = val // 10

            new = ListNode(digit)
            prev.next = new
            prev = new

            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
        
        return start.next


            