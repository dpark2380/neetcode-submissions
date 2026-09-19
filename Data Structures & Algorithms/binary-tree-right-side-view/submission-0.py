# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([(root)])
        ans = []

        while queue:
            length = len(queue)
            
            for _ in range(length - 1):
                cur = queue.popleft()

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            cur = queue.popleft()
            ans.append(cur.val)

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

        return ans


