# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        
        queue = deque([root])

        while queue:
            length = len(queue)
            
            curarr = []
            for _ in range(length):
                cur = queue.popleft()
                curarr.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
            ans.append(curarr)
        
        return ans

