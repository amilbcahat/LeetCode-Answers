# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node.val == 0 : 
                return False 
            elif node.val == 1 : 
                return True 

            return dfs(node.left) and dfs(node.right) if node.val == 3 else dfs(node.left) or dfs(node.right)

        return dfs(root)