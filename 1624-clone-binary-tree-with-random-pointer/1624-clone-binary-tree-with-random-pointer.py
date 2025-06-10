# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
            
        oldToCopy = {None: None}
        
        # First pass: Create all nodes and store mapping
        def createNodes(node):
            if not node:
                return None
            
            copy = NodeCopy(node.val)
            oldToCopy[node] = copy
            
            createNodes(node.left)
            createNodes(node.right)
            
        createNodes(root)
        
        # Second pass: Set up all pointers (left, right, random)
        def linkNodes(node):
            if not node:
                return None
                
            copy = oldToCopy[node]
            copy.left = oldToCopy[node.left]
            copy.right = oldToCopy[node.right] 
            copy.random = oldToCopy[node.random]
            
            linkNodes(node.left)
            linkNodes(node.right)
            
        linkNodes(root)
        
        return oldToCopy[root]