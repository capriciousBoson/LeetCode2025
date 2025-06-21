# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        inorder_idx = {inorder[i]:i for i in range(n)}
        pos_idx = n-1

        def build(inorder_start, inorder_end):
            nonlocal pos_idx
            if inorder_start > inorder_end:
                return

            

            root_val = postorder[pos_idx]
            pos_idx -= 1

            root_idx = inorder_idx[root_val]
            root = TreeNode(postorder.pop())

            root.right = build(root_idx+1, inorder_end)
            root.left = build(inorder_start, root_idx-1)

            return root
        return build(0,n-1)


        