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
        # DFS traversal 
        verticalMap = defaultdict(list)
        max_col = float("-inf")
        min_col = float("inf")
        def dfs(node, r, c):
            nonlocal max_col, min_col
            if not node: 
                return 

            max_col = max(max_col, c)
            min_col = min(min_col, c)
            verticalMap[c].append((r, node.val))
            dfs(node.left, r + 1, c - 1)
            dfs(node.right, r + 1, c + 1)

        dfs(root, 0, 0)

        print(verticalMap, min_col, max_col)
        res = []
        for col in range(min_col, max_col + 1): 
            verticalMap[col].sort(key=lambda x: x[0])
            colVals = [val for row, val in verticalMap[col]]
            res.append(colVals)

        return res

        # BFS traversal
        # if not root: 
        #     return []

        # q = deque([(root, 0)])
        # verticalMap = defaultdict(list)
        # max_col = float("-inf")
        # min_col = float("inf")
        # while q: 
        #     for i in range(len(q)):
        #         #We track and map with the x coordinate
        #         node, x = q.popleft()
        #         verticalMap[x].append(node.val)
        #         max_col = max(x, max_col)
        #         min_col = min(x, min_col)
        #         if node and node.left:
        #             q.append([node.left, x - 1])
        #         if node and node.right:
        #             q.append([node.right, x + 1])

        # length = max_col - min_col + 1

        # res = [[]] * length
        # for key in verticalMap.keys():
        #     res[key - min_col] = verticalMap[key]

        # return res 