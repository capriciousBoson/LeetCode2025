from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = defaultdict(list)

        def traverse(l, node):
            if not node:
                return
            levels[l].append(node.val)
            traverse(l+1, node.left)
            traverse(l+1, node.right)

        traverse(0,root)
        res = []
        for i in range(len(levels)):
            res.append(levels[i][-1])

        return res





        