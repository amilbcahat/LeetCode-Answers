"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque([root])

        while q: 
            level = []
            for i in range(len(q)): 
                node = q.popleft()
                level.append(node)
                if node and node.left : 
                    q.append(node.left)
                if node and node.right: 
                    q.append(node.right)
            
            for i in range(len(level) - 1): 
                level[i].next = level[i + 1]
                level[i + 1].next = None 

        return root