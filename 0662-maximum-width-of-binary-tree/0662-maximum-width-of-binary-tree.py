# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 1)])
        res = 1

        while q: 
            levelSize = len(q)
            start = end = 0 
            for i in range(levelSize):
                node, val = q.popleft()
                if node.left:
                    q.append((node.left, 2 * val))
                if node.right:
                    q.append((node.right, (2 * val) + 1))

                if i == 0: 
                    start = val 
                elif i == levelSize - 1:
                    end = val 

            res = max(res, end - start + 1)

        return res
