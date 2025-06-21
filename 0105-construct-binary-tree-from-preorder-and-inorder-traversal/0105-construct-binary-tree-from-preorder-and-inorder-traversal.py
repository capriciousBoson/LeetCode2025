# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        inorder_index = {inorder[i]:i for i in range(n)}
        pre_idx = 0

        def build(inorder_start, inorder_end):
            nonlocal pre_idx
            if inorder_start>inorder_end: return

            root = TreeNode(preorder[pre_idx])
            root_idx = inorder_index[preorder[pre_idx]]

            pre_idx += 1

            root.left = build(inorder_start, root_idx-1)
            root.right = build(root_idx+1, inorder_end)
            return root
        
        return build(0,n-1)




        