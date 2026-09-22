# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2

        carry = 0

        start = ListNode()
        prev = start

        while cur1 or cur2 or carry:
            if cur1:
                v1 = cur1.val
            else:
                v1 = 0
            
            if cur2:
                v2 = cur2.val
            else:
                v2 = 0

            if not cur1 and not cur2:
                if carry == 1:
                    new = ListNode(1)
                    prev.next = new
                    break
            
            val = v1 + v2 + carry

            if val > 9:
                rem = val % 10
                new = ListNode(rem)
                prev.next = new
                prev = new
                carry = 1
            else:
                new = ListNode(val)
                prev.next = new
                prev = new
                carry = 0
            
            if cur1: 
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next


        return start.next
        