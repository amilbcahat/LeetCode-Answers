# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []

        q = deque([root])
        zigzag = False #this is for next level
        ans = []
        while q: 
            level = []
            for i in range(len(q)):
                if zigzag:
                    node = q.pop()
                    level.append(node.val)
                    if node.right: 
                        q.appendleft(node.right)
                    if node.left: 
                        q.appendleft(node.left)
                else:
                    node = q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if len(level) > 0 :   
                ans.append(level[:])
                zigzag = not zigzag 

        return ans
                
