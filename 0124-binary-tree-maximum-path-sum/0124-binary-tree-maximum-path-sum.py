# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')

        def traverse(node):
            nonlocal res
            if not node:
                print(f"\nat node : {node} ")
                return -float('inf')
            print(f"\nat node : {node.val} --------------------------------------------------------------------------")
            

            l = traverse(node.left)
            r = traverse(node.right)

            print(f"finding res in {res,l, r, l+node.val, r+node.val, l+node.val+r, node.val}")
            res = max(res,l, r, l+node.val, r+node.val, l+node.val+r, node.val)
            print(f"at node: {node.val} leftpath = {l}, right_path= {r}, res : {res}")

            if l == r== -float('inf') :  return node.val
            print(f"going to final return l, r : {l,r}")
            return max(l+node.val, r+node.val, node.val)
        traverse(root)
        return res
        