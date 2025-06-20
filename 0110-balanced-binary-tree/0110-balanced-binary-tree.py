# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(h, node):
            if not node:
                return h
            l = height(h+1, node.left)
            r = height(h+1, node.right)
            if l==-1 or r==-1:
                return -1
            if abs(l-r) > 1: return -1
            return max(l,r)

        if not root: return True
        h = height(0, root)
        if h==-1: return False
        return True