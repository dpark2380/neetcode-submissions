# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == p or root == q:
            return root
        
        queue = deque([root])

        v1 = p.val
        v2 = q.val

        while queue:
            cur = queue.popleft()

            if v1 <= cur.val and v2 >= cur.val:
                return cur
            elif v2 <= cur.val and v1 >= cur.val:
                return cur
            
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        
        return cur
