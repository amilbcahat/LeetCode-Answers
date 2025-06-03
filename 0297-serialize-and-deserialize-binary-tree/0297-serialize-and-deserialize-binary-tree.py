# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        sb = []
        self.serHelper(root, sb)
        return ''.join(sb)

    def serHelper(self, root, sb): 
        if root is None:
            sb.append("#,")
            return 

        sb.append(str(root.val) + ',')
        self.serHelper(root.left, sb)
        self.serHelper(root.right, sb)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        nodes = data.split(',')
        nodes.pop()
        self.index = 0
        return self.deHelper(nodes)

    def deHelper(self, nodes):
        if self.index >= len(nodes): 
            return None 
        
        value = nodes[self.index]
        self.index += 1

        if value == "#": 
            return None
        
        root = TreeNode(int(value))
        root.left = self.deHelper(nodes)
        root.right = self.deHelper(nodes)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))