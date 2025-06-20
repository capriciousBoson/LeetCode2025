# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        a,b = float('inf'),-float('inf')

        d = 0
        
        def traverse(i,j,node):
            nonlocal a
            nonlocal b
            nonlocal d

            if not node: return
            a = min(a,j)
            b = max(b,j)
            d = max(d, i)

            levels[(i,j)].append(node.val)
            traverse(i+1, j-1, node.left)
            traverse(i+1, j+1, node.right)
        traverse(0,0, root)
        
        ans = []
        for j in range(a,b+1):
            t = []
            for i in range(d+1):
                t += sorted(levels[(i,j)])
            ans.append(t)



        
        return ans
        
