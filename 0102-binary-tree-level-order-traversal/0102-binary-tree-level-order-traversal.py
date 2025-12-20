# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        #Empty array 
        if not root : 
            return ans 
        
        q = deque([root])

        while (q) : 
            n = len(q)
            level = []
            for i in range(0,n):
                pop_node = q.popleft()
                level.append(pop_node.val)
                if pop_node.left: 
                    q.append(pop_node.left)
                if pop_node.right: 
                    q.append(pop_node.right)

            if level: 
                ans.append(level[:])
                level.clear()

        return ans  
