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

        def build(inorder_start, inorder_end, preorder):
            if inorder_start <0 or inorder_end >n:
                return None
            if not len(preorder):
                return None

            x = preorder[0]
            root_idx = inorder_index[x]
            if inorder_start > inorder_end: return None



            root = TreeNode(preorder.pop(0))

            

            root.left = build(inorder_start, root_idx-1, preorder)
            root.right = build(root_idx+1, inorder_end, preorder)
            return root
        
        return build(0,n-1, preorder)




        