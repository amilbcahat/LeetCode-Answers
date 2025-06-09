"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root: 
            return ""

        q = deque([root])
        sb = []
        while q: 
            node = q.popleft()
            if node is None: 
                sb.append("null,")
                continue 
            
            sb.append(f"{node.val},")

            for child in node.children: 
                q.append(child)
            q.append(None)

        return "".join(sb)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
            
        nodes = data.split(",")
        root = Node(int(nodes[0]))
        q = deque([root])
        
        i = 1 
        while q: 
            if q: 
                parent = q.popleft()
            else:
                break 

            while i < len(nodes) and nodes[i] != "null" and parent: 
                child = Node(int(nodes[i]))
                parent.children.append(child)
                q.append(child)
                i += 1

            i += 1

        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))