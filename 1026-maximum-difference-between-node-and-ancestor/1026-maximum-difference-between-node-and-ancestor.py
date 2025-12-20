# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxDiff = float("-inf")
        def dfs(node, curMax, curMin):
            nonlocal maxDiff
            if not node:
                return 

            curMax = max(curMax, node.val)
            curMin = min(curMin, node.val)
            maxDiff = max(maxDiff, node.val - curMin, curMax - node.val)

            dfs(node.left, curMax, curMin)
            dfs(node.right, curMax, curMin)

        dfs(root, float("-inf"), float("inf"))

        return maxDiff

            