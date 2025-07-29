class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #Editorial please check always
        # This will help in understanding that - https://math.stackexchange.com/a/3961816
        # Backtracking
        # n = len(graph)
        # res = []
        # def dfs(node, path):
        #     nonlocal res 
        #     if node == n - 1: 
        #         res.append(list(path))
        #         return

        #     for nei in graph[node]: 
        #         path.append(nei)
        #         dfs(nei, path) 
        #         path.pop()

        # dfs(0, [0])

        # return res

        #Top Down Approach 
        # allPathsToTarget(currNode)={currNode+allPathsToTarget(nextNode)}
        target = len(graph) - 1

        @lru_cache(maxsize=None)
        def all_paths_to_target(node): 
            if node == target: 
                return [[target]]

            path_to_target_from_this_node = []
            for nei in graph[node]: 
                for path in all_paths_to_target(nei): 
                    path_to_target_from_this_node.append([node] + path)
            
            return path_to_target_from_this_node

        return all_paths_to_target(0)







        
6