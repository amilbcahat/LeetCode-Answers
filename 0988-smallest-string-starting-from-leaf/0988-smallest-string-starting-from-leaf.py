# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = None 
        path = []

        def dfs(node , path) : 
            nonlocal ans 
           
            if not node : 
                return 

            #We did this by taking out path 

            path.append(chr(node.val + ord("a")))

            if not node.left and not node.right : 
                rev_path = "".join(path[::-1])
                #Good Lexographical check 
                if ans is None or rev_path < ans : 
                    ans = rev_path

            dfs(node.left , path)
            dfs(node.right, path)
            path.pop()

        dfs(root , [])

        return ans 
