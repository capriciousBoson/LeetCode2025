# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def height(node):
            nonlocal res
            if not node:
                return 0
            l = height(node.left)
            r = height(node.right)

            res = max(res, l+r)
            return max(l,r)+1
        height(root)
        return res