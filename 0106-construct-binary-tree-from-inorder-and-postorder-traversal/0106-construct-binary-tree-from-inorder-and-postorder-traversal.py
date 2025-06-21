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

        def build(inorder_start, inorder_end, postorder):
            if not postorder:
                return

            root_val = postorder[-1]
            root_idx = inorder_idx[root_val]

            root = TreeNode(postorder.pop())

            s = root_idx-inorder_start

            root.left = build(inorder_start, root_idx-1, postorder[0:s])
            root.right = build(root_idx+1, inorder_end, postorder[s:])
            return root
        return build(0,n-1 , postorder[:])


        