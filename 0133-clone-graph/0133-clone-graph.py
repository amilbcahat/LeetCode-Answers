"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: 
            return None 

        oldToCopy = {None: None}
        def dfs(node): 
            if node in oldToCopy:
                return oldToCopy[node]
                
            copy = Node(node.val)
            oldToCopy[node] = copy 

            for nei in node.neighbors: 
                copy.neighbors.append(dfs(nei))

            return copy 

        return dfs(node)
            
        