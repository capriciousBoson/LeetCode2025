# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)

        def levelorder(l,node):
            if not node:
                return
            
            levels[l].append(node.val)
            levelorder(l+1, node.left)
            levelorder(l+1, node.right)

        levelorder(0, root)
        res = []
        for i,level in enumerate(levels.values()):
            if i%2!=0:
                res.append(level[::-1])
            else:
                res.append(level[:])
        return res
