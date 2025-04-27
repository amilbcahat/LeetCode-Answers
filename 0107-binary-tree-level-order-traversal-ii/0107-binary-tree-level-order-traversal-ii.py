# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:    
        levels = []
        if not root: 
            return levels

        def dfs(node, level): 
            if len(levels) == level: 
                levels.append([])

            levels[level].append(node.val)

            if node.left: 
                dfs(node.left, level + 1)

            if node.right: 
                dfs(node.right, level + 1)

        dfs(root, 0)
        return levels[::-1]

        
        # Through Level Order Travsersal
        # if root is None: 
        #     return []
        # q = deque([root])
        # res = []
        # while q: 
        #     level = []
        #     for i in range(len(q)): 
        #         node = q.popleft()
        #         level.append(node.val)
        #         if node and node.left: 
        #             q.append(node.left)
        #         if node and node.right: 
        #             q.append(node.right)

        #     res.append(level)
        # return res[::-1]