# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def height(node):
            if not node:
                return 0,0
            l, ld = height(node.left)
            r, rd = height(node.right)
            return max(l,r)+1, max(l+r, ld, rd)

        h, d = height(root)
        return d