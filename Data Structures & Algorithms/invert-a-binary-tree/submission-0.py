# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def reversebinarytree(node):
            if not node:
              return 

            node.left, node.right = node.right, node.left

            reversebinarytree(node.left)
            reversebinarytree(node.right)
        reversebinarytree(root)
        return root   



        