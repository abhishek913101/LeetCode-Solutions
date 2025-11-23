# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Validates if a binary tree is a valid Binary Search Tree (BST) 
        using recursion with upper and lower bounds.
        """
        def valid(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            return valid(node.left, min_val, node.val) and valid(node.right, node.val, max_val)
        return valid(root, float('-inf'), float('inf'))