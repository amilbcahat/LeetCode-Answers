class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #Editorial please check always
        # This will help in understanding that - https://math.stackexchange.com/a/3961816
        n = len(graph)
        res = []
        def dfs(node, path):
            nonlocal res 
            if node == n - 1: 
                res.append(list(path))
                return

            for nei in graph[node]: 
                path.append(nei)
                dfs(nei, path) 
                path.pop()

        dfs(0, [0])

        return res



        
