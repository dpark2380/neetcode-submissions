# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float("-inf"), float("inf"))
    
    def dfs(self, node, left, right):
        if not node:
            return True

        # We recursively adjust the interval in which the node's value can lie in.
        if not (left < node.val < right):
            return False
        
        # For the left subtree, the values must be greater than left and less than the current node's value.
        # Similar for right subtree. 
        return self.dfs(node.left, left, node.val) and self.dfs(node.right, node.val, right)

        