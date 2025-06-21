# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getHeight(node, dir):
            height = 1
            while node:
                if dir=="l": node = node.left
                else: node = node.right
                height += 1
            return height
        if not root: return 0  
        lh = getHeight(root.left, "l")
        rh = getHeight(root.right, "r")
        if lh==rh: return 2**lh-1
        else: return 1 + self.countNodes(root.left) + self.countNodes(root.right)
