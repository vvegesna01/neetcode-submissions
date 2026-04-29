# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1, 2, 3, 4, 5, 6, 7, 
        # 1, 3, 2, 7, 6, 5, 4

        # 3, 2, 1
        # 3, 1, 2


        if not root:
            return None

        # swap children
        temp = root.left
        root.left = root.right
        root.right = temp

        # call recursive on both children
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root