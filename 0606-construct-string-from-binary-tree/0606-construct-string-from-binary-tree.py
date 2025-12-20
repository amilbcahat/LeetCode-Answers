# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ""
        def dfs(node):
            if not node : 
                return ""

            result  = str(node.val)
            
            #The checking of node.right here , actually is very important , as it still checks for node.left and if it is not there , it will add ()
            if node.left or node.right : 
                result += "(" + dfs(node.left) + ")"
            
            if node.right : 
                result += "(" + dfs(node.right) + ")"

            return result

        return dfs(root)

         
            