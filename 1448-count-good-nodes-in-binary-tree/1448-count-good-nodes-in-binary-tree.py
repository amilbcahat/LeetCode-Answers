# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

         
        def dfs(node,cur_max):
            if not node:
                return 0 

            if node.val >= cur_max:
                res = 1
            else:
                res = 0 

            maxi = max(cur_max, node.val)
            res += dfs(node.left, maxi)
            res += dfs(node.right, maxi)
            return res

        return dfs(root, root.val)


