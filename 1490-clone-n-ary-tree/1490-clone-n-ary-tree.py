"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        oldToCopy = {None: None}

        def linkNodes(node):
            if not node: 
                return None

            copy = Node(node.val)
            oldToCopy[node] = copy 

            for child in node.children:
                copy.children.append(linkNodes(child))

            return copy 

        return linkNodes(root) if root else None
            