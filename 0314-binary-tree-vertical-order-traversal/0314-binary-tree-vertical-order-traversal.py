# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []

        q = deque([(root, 0)])
        verticalMap = defaultdict(list)
        while q: 
            for i in range(len(q)):
                #We track and map with the x coordinate
                node, x = q.popleft()
                verticalMap[x].append(node.val)
                if node and node.left:
                    q.append([node.left, x - 1])
                if node and node.right:
                    q.append([node.right, x + 1])

        res = []
        for key in sorted(verticalMap.keys()):
            res.append(verticalMap[key])

        return res 