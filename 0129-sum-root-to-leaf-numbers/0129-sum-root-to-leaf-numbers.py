# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0

        def dfs(cur, curTotal):
            if not cur:
                return 0

            curTotal = curTotal * 10 + cur.val
            if not cur.left and not cur.right:
                return curTotal

            return dfs(cur.left, curTotal) + dfs(cur.right, curTotal)

        return dfs(root, 0)
        