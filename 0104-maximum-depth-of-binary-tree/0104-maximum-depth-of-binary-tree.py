# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:


        def height(h, root):
            if not root:
                return h
            h1 = height(h+1, root.left) 
            h2 = height(h+1, root.right) 
            # print(f"for node {root.val} left, right: {h1, h2}")
            return max(h1, h2)

        return height(0, root)
        