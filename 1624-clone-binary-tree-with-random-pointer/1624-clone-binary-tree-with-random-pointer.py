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
        
        def linkNodes(node):
            if not node:
                return None

            #Copy already is there
            if node in oldToCopy: 
                return oldToCopy[node]
            
            copy = NodeCopy(node.val)
            oldToCopy[node] = copy
            copy.left = linkNodes(node.left) #All are kind of same logic , we are just traversing throughout
            copy.right = linkNodes(node.right)
            copy.random = linkNodes(node.random)
            return copy
            
        linkNodes(root)
        
        return oldToCopy[root]