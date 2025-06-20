# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def traverse(left_node, right_node):
            if not left_node and not right_node:
                return True
            if (not left_node) or (not right_node):
                return False
            
            if left_node.val != right_node.val:
                return False
            
            if not (traverse(left_node.left, right_node.right) and traverse(left_node.right, right_node.left)):
                return False
            return True
        if not root.left and not root.right: return True
        if (not root.left) or (not root.right): return False
        
        return traverse(root.left, root.right)

        