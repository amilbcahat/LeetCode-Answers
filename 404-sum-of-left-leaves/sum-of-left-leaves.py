# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        res = 0 
        def dfs(node, left):
            nonlocal res 
            if not node : 
                return 0 

            
            if left and (not node.left and not node.right):
                res += node.val
            if node.left :
                dfs(node.left , True)
            if node.right : 
                dfs(node.right, False)

            return res 

        return dfs(root , False )
            