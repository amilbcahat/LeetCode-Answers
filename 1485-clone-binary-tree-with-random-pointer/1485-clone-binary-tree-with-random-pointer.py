# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None 


        oldToCopy = {None: None}

        def linkNodes(node):
            if node in oldToCopy:
                return oldToCopy[node]

            copy = NodeCopy(node.val)
            oldToCopy[node] = copy 
            copy.left = linkNodes(node.left)
            copy.right = linkNodes(node.right)
            copy.random = linkNodes(node.random)
            return copy 

        return linkNodes(root)