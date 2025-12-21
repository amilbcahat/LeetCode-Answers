class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #Check DFS Video of AlgoZenith
        visit = defaultdict(int)

        def dfs(node, clr): 
            visit[node] = clr
            ans = True
            for nei in graph[node]: 
                if nei not in visit: 
                    # Flips the color here
                    # We could also use clr ^ 1
                    ans = dfs(nei, 3 - clr)
                elif visit[node] == visit[nei]: 
                    return False
            return ans


        for i in range(len(graph)): 
            if i not in visit: 
                if not dfs(i, 1): 
                    return False

        # To note, no of ways bipartite graph can be formed
        # m = No. of components 
        # 2 ^ m
        # Because each node if designated with a color 1 or 2, decides the component there, so that start node has 2 choices
        # Equivalent definitions of a bipartite graph:

        # There is no cycle of odd length

        # we can split the nodes of the graph
        # (vertex set of the graph) into 2 subsets so
        # that there is all the edges go from 1 subset
        # to the other subset.

        # 3.The graph should be bi-colourable.
        return True
