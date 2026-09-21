# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder

        valmap = {}
        for i in range(len(inorder)):
            valmap[inorder[i]] = i

        self.indices = valmap
        # index of the next unused element in preorder.
        self.preIdx = 0

        return self.helper(0, len(inorder) - 1)
    
    def helper(self, left, right):
        if left > right:
            return None

        # Root is the next element in the preorder list.
        root = TreeNode(self.preorder[self.preIdx])
        # For the next recursive call.
        self.preIdx += 1

        # Index of the root in the inorder array, allows us to split 
        # left and right subtree.
        i = self.indices[root.val]

        # Inclusive indices.
        root.left = self.helper(left, i - 1)
        root.right = self.helper(i + 1, right)

        return root







