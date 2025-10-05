class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visit = defaultdict(int)
        is_bipartite = True
        def dfs(node, clr): 
            nonlocal is_bipartite
            visit[node] = clr
            ans = False
            for nei in graph[node]: 
                if nei not in visit: 
                    dfs(nei, 3 - clr)
                elif visit[node] == visit[nei]: 
                    is_bipartite = False


        for i in range(len(graph)): 
            if i not in visit: 
                dfs(i, 1)

        return is_bipartite
