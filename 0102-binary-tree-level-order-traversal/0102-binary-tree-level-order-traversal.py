# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        
        def bfs(i, root):
            if not root:
                return
            levels[i].append(root.val)
            if root.left:
                bfs(i+1, root.left)
            if root.right:
                bfs(i+1, root.right)
        
        bfs(0,root)
        return [levels[i] for i in range(len(levels))]
            
        