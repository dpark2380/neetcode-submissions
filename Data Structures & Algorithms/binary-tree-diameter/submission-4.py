# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.hmax = 0
        self.height(root)
        return self.hmax

    def height(self, root):
        if not root:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)

        diam = left + right
        if diam > self.hmax:
            self.hmax = diam
        
        return 1 + max(left, right)
