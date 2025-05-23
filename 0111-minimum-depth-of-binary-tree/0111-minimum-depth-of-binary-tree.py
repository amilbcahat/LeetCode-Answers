# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: 
                return 0 

            if not root.left:
                return 1 + dfs(root.right)

            if not root.right: 
                return 1 + dfs(root.left)

            return 1 + min(dfs(root.left), dfs(root.right))

        return dfs(root)


        # By BFS 
        # if not root: 
        #     return 0 

        # q = deque([root])

        # levels = 1
        # while q: 
        #     for i in range(len(q)): 
        #         node = q.popleft()
        #         if node.left: 
        #             q.append(node.left)
        #         if node.right: 
        #             q.append(node.right)

        #         if not node.left and not node.right: 
        #             #first leaf node where, it does not have children , would have the answer
        #             return levels 

        #     levels += 1
        return -1


            