# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getHeight(node):
            height = 0
            while node:
                node = node.left
                height += 1
            return height
        
        if not root: return 0
        stack = [root]
        result = 0
        while stack:
            node = stack.pop()
            heightLeft = getHeight(node.left)
            heightRight = getHeight(node.right)
            if heightLeft == heightRight:
                result += (1 << heightLeft)
                if node.right: stack.append(node.right)
            else:
                result += (1 << heightRight)
                if node.left: stack.append(node.left)
        return result