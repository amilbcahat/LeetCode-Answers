# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        def preorder(node): 
            if not node: 
                return None 

            stack.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        for i in range(len(stack) - 1): 
            last = stack.pop()
            stack[-1].right = last
            stack[-1].left = None
        
        return stack[-1] if stack else None

            