# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = defaultdict(list)
        def turnToGraph(node):
            if not node:
                return 

            if node.right: 
                adj[node.val].append(node.right.val)
                adj[node.right.val].append(node.val)

            if node.left:
                adj[node.val].append(node.left.val)
                adj[node.left.val].append(node.val)

            turnToGraph(node.left)
            turnToGraph(node.right)

        turnToGraph(root)

        q = deque([start])
        visit = set()
        level = -1
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node in visit:
                    continue 

                visit.add(node)
                for nei in adj[node]:
                    if nei not in visit:
                        q.append(nei)

            level += 1

        return level