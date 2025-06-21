# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = defaultdict(TreeNode)
        neighbors = []
        visited = [target]

        def dfs(node):
            if not node:
                return
            
            if node.left:
                parent[node.left] = node
                dfs(node.left)
            if node.right:
                parent[node.right] = node
                dfs(node.right)
        
        dfs(root)
        res = []
        # print(f"parents : {parent}")
        def crawl(d, node):
            if not node:
                return
            if d==k:
                res.append(node.val)
            
            if node.left:
                if node.left not in visited:
                    visited.append(node.left)
                    crawl(d+1, node.left)

            if node.right:
                if node.right not in visited:
                    visited.append(node.right)
                    crawl(d+1, node.right)

            if node in parent:
                if parent[node] not in visited:
                    visited.append(parent[node])
                    crawl(d+1, parent[node])
        crawl(0,target)

        return res



            





                
            
        