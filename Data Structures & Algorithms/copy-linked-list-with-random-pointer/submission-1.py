"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    map = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # Returning copy if it already exists. 
        if head in self.map:
            return self.map[head]

        new = Node(head.val)
        self.map[head] = new
        new.next = self.copyRandomList(head.next)
        # Need to use .get to handle None pointers safely. 
        new.random = self.map.get(head.random)

        return new

            



        