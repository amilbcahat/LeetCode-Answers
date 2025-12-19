# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        ans = 1

        def dfs(node, seq, par):
            nonlocal ans
            if not node:
                return 

            # print(par, node.val, seq, par + 1 == node.val)

            if par + 1 == node.val :
                seq += 1
            else:
                seq = 1

            ans = max(ans, seq)
            
            dfs(node.left, seq, node.val)

            dfs(node.right, seq, node.val)

        dfs(root, 0, 30002)
        return ans
    
