# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(list)


        def dfs(l,i,node):
            if not node:
                return
            levels[(l)].append((i, node.val))
            dfs(l+1, 2*i+1, node.left)
            dfs(l+1, 2*i+2, node.right)

        dfs(0,0,root)
        res = 1
        for l, nodes in levels.items():
            # print(f"nodes at level {l} : {nodes}")
            x = nodes[-1][0] - nodes[0][0] + 1
            res = max(res, x)
        return res

            

            



        