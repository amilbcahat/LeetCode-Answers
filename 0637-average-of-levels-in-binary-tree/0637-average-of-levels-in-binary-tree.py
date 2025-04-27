# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = []

        if not root:
            return levels
        
        def dfs(node, level): 
            if len(levels) == level: 
                levels.append([0, 0])

            levels[level] = [node.val + levels[level][0], 1 + levels[level][1]]

            if node.right: 
                dfs(node.right, level + 1)
            
            if node.left: 
                dfs(node.left, level + 1)
                                
        dfs(root, 0)

        return [(total / levelNodeCount) for total, levelNodeCount in levels]
