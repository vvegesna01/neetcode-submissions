# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            height = abs(left - right)

            if left >= 0 and right >= 0 and height <= 1:
                return 1 + max(left, right)
            else:
                return -1
        
        if dfs(root) == -1:
            return False
        else:
            return True
