# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])

        while queue:
            cur = queue.popleft()

            if cur.val == subRoot.val:
                ret = self.isSameTree(cur, subRoot)
                if ret:
                    return True
            
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        
        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif p and not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)  