# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        def dfs(node , s):
            nonlocal ans 
            
            if not node.left and not node.right : 
                ans += (int(s + str(node.val)))
                return 

            if node.left :
                dfs(node.left , s + str(node.val))
            if node.right : 
                dfs(node.right , s + str(node.val))

        

        dfs(root , "")
        print(ans)
        return ans


