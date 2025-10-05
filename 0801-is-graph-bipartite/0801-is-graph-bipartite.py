class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visit = defaultdict(int)
        def dfs(node, clr): 
            visit[node] = clr
            ans = True
            for nei in graph[node]: 
                if nei not in visit: 
                    ans = dfs(nei, 3 - clr)
                elif visit[node] == visit[nei]: 
                    return False
            return ans


        for i in range(len(graph)): 
            if i not in visit: 
                if not dfs(i, 1): 
                    return False

        return True
